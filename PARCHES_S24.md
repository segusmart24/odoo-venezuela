# Parches de Segusmart24 sobre la localización de Binaural

Esta rama (`19.0-s24`) es la rama `19.0` de `binaural-dev/odoo-venezuela` más los parches de esta lista, cada uno en su propio commit. El proyecto `segusmart24/grupo-odoo` usa esta rama como submódulo.

Regla: solo correcciones mínimas que no cambian el comportamiento (avisos, metadatos), que evitan un error de instalación o que quitan código con licencia que no podemos redistribuir. Cualquier cambio funcional se hace heredando desde un módulo propio `s24_*`. Cualquier cambio funcional se hace heredando desde un módulo propio `s24_*`, nunca aquí.

| Fecha | Módulo | Cambio | Motivo |
| --- | --- | --- | --- |
| 2026-10-24 | l10n_ve_donation | `author`, `website` y `license` (LGPL-3) en `__manifest__.py` | Avisos "Missing author/license key" |
| 2026-10-24 | l10n_ve_payment_extension | `tax.unit.available_date` con valor por defecto (fecha del día) | `ERROR odoo.schema: column "available_date" ... contains null values` al instalar retenciones sobre la unidad tributaria sin fecha de `l10n_ve_accountant` |
| 2026-10-24 | od_journal_sequence | **Módulo eliminado.** `l10n_ve_invoice` y `l10n_ve_exchange_difference` dependen de `s24_ve_secuencia_diario` (producto `s24-odoo-ve`), escrito desde cero con los mismos nombres técnicos; la vista de `l10n_ve_invoice` que heredaba `od_journal_sequence.view_move_form` hereda `account.view_move_form` (resultado idéntico: número editable) | `od_journal_sequence` es un módulo de pago (OPL-1) que no se puede redistribuir |
| 2026-10-24 | l10n_ve_accountant, l10n_ve_location, l10n_ve_payment_extension | `_sql_constraints` pasan a `models.Constraint` (los de `account.move`, vacíos, se quitan) | En Odoo 19 `_sql_constraints` se ignora: las restricciones no existían y el log avisaba |
| 2026-10-24 | varios | `_description` en 9 modelos; `_name` explícito en `account.payment` y `account.payment.register` | Avisos del registro de modelos |
| 2026-10-24 | varios | Etiquetas distintas para 15 campos que repetían la de otro campo, con su traducción en `es_VE.po`; se quita una definición duplicada de `show_field_currency_system` | Avisos "Two fields ... have the same label" |
| 2026-10-24 | varios | XPath con `hasclass()` en lugar de `@class`; el bloque de vencimiento de `l10n_ve_invoice` se ubica por `@name='due_date'` (mismo nodo que antes) | Avisos "Error-prone use of @class". Verificado: las vistas combinadas quedan iguales |
| 2026-10-24 | l10n_ve_accountant | Se quita la página "Foreign currency" de la factura, protegida por un grupo que ya no existe | Aviso de grupo inexistente; la página ya era invisible para todos y la especificación de Binaural dice que no debe existir |
| 2026-10-24 | varios | Grupo `base.group_user` en 15 reglas de acceso sin grupo | Aviso de regla de acceso sin grupo; los usuarios internos conservan el mismo acceso |
| 2026-10-24 | l10n_ve_payment_extension | IDs de 3 accesos sin el prefijo `account.` | Aviso "Creating record account.access_... in module" |
| 2026-10-24 | varios | `self._context` → `self.env.context`; `_()` fuera de las definiciones de campos; `@api.constrains` sin campos relacionados no almacenados | Avisos de obsolescencia y de traducción |
| 2026-10-24 | l10n_ve_igtf, l10n_ve_accountant, l10n_ve_stock_account, l10n_ve_payment_extension, l10n_ve_fiscal_lock_days | Campos del asistente de pago con IGTF almacenados como `amount`; `precompute=False` explícito donde Odoo ya no precalculaba; se quitan un `default` y una lista de selección redundantes en campos relacionados | Avisos de campos calculados; sin cambio de comportamiento |

## Cómo traer las actualizaciones de Binaural

```
git remote add binaural https://github.com/binaural-dev/odoo-venezuela.git   # una sola vez
git fetch binaural 19.0
git checkout 19.0-s24
git rebase binaural/19.0        # los parches quedan encima de lo nuevo
git push --force-with-lease origin 19.0-s24
```

Si Binaural ya corrigió algo de esta tabla, el rebase descarta ese parche: se borra su fila. Después, en `grupo-odoo`, se actualiza el puntero del submódulo en una rama de desarrollo y se prueba en Odoo.sh antes de pasarlo a producción.
