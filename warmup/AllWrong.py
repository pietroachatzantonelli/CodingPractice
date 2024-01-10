def getWrongAnswers(N: int, C: str) -> str:
  wrongstring=''
  for answer in list(C):
    if answer=='A':
      wronganswer='B'
    if answer=='B':
      wronganswer='A'
    wrongstring=wrongstring+wronganswer
  return wrongstring