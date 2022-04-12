from db_notes import Note, Session, engine
note_session = Session(bind=engine)

title = ""
note = ""

new_note = Note(note_title=title, note_content=note)
note_session.add(new_note)
note_session.commit()

