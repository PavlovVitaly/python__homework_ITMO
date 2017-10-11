CREATE TABLE IF NOT EXISTS notebook (
  id           INTEGER PRIMARY KEY                                                                                                                                                                         AUTOINCREMENT,
  name_of_note TEXT     NOT NULL,
  text_of_note TEXT NOT NULL                                                                                                                                                                               DEFAULT '',
  status       TEXT NOT NULL                                                                                                                                                                               DEFAULT 'Выполняется',
  start_date   DATETIME NOT NULL                                                                                                                                                                           DEFAULT CURRENT_TIMESTAMP,
  end_date     DATETIME NOT NULL                                                                                                                                                                           DEFAULT CURRENT_TIMESTAMP
)
