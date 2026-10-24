# Parches de Segusmart24 sobre la localización de Binaural

Esta rama (`19.0-s24`) es la rama `19.0` de `binaural-dev/odoo-venezuela` más los parches de esta lista, cada uno en su propio commit. El proyecto `segusmart24/grupo-odoo` usa esta rama como submódulo.

Regla: solo correcciones mínimas que no cambian el comportamiento (avisos, metadatos). Cualquier cambio funcional se hace heredando desde un módulo propio `s24_*`, nunca aquí.

| Fecha | Módulo | Cambio | Motivo |
| --- | --- | --- | --- |
| 2026-10-24 | l10n_ve_donation | `author`, `website` y `license` (LGPL-3) en `__manifest__.py` | Eliminar los avisos "Missing author/license key" que ponían los builds de Odoo.sh en amarillo |

## Cómo traer las actualizaciones de Binaural

```
git remote add binaural https://github.com/binaural-dev/odoo-venezuela.git   # una sola vez
git fetch binaural 19.0
git checkout 19.0-s24
git rebase binaural/19.0        # los parches quedan encima de lo nuevo
git push --force-with-lease origin 19.0-s24
```

Si Binaural ya corrigió algo de esta tabla, el rebase descarta ese parche: se borra su fila. Después, en `grupo-odoo`, se actualiza el puntero del submódulo en una rama de desarrollo y se prueba en Odoo.sh antes de pasarlo a producción.
