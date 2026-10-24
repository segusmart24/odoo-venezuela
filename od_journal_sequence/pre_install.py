# -*- coding: utf-8 -*-
# Parche S24 (ver PARCHES_S24.md): evita el ERROR de esquema
# "column sequence_id ... contains null values" cuando el módulo se instala
# en una base que ya tiene diarios. Se llena la columna con una secuencia
# provisional; create_journal_sequences la reemplaza y la elimina.

PROVISIONAL = "od_journal_sequence: provisional"


def prefill_journal_sequences(env):
    cr = env.cr
    cr.execute("SELECT to_regclass('account_journal') IS NOT NULL")
    if not cr.fetchone()[0]:
        return
    cr.execute("SELECT count(*) FROM account_journal")
    if not cr.fetchone()[0]:
        return
    cr.execute("SELECT 1 FROM information_schema.columns "
               "WHERE table_name = 'account_journal' AND column_name = 'sequence_id'")
    if cr.fetchone():
        return
    sequence = env["ir.sequence"].sudo().create({
        "name": PROVISIONAL, "implementation": "no_gap", "padding": 4,
    })
    cr.execute("ALTER TABLE account_journal ADD COLUMN sequence_id integer")
    cr.execute("UPDATE account_journal SET sequence_id = %s", [sequence.id])
