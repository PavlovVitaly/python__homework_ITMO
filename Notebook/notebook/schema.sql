CREATE TABLE IF NOT EXISTS notebook (
  id           INTEGER PRIMARY KEY                                                                                     AUTOINCREMENT,
  name_of_note TEXT     NOT NULL,
  text_of_note TEXT NOT NULL                                                                                           DEFAULT "",
  status       INT  NOT NULL                                                                                           DEFAULT 1,
  start_date   DATETIME NOT NULL                                                                                       DEFAULT CURRENT_TIMESTAMP,
  end_date     DATETIME NOT NULL                                                                                       DEFAULT CURRENT_TIMESTAMP
)
