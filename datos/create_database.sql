CREATE TABLE "movimientos" (
    "id"    INTEGER,
    "tipo_movimiento"    TEXT NOT NULL,
    "concepto"    TEXT NOT NULL,
    "fecha"    TEXT NOT NULL,
    "cantidad"    REAL NOT NULL,
    "categoria"    INTEGER,
    PRIMARY KEY("id" AUTOINCREMENT)
);