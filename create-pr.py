import sys, os

# MNG-246-fix-detekt-config
branchName = os.popen("git rev-parse --abbrev-ref HEAD").read().replace('\n', '')

wordsList = branchName.split('-')
projectCode = wordsList[0]
ticketNumber = wordsList[1]
titleList = wordsList[2:]

title = " ".join(titleList).title()
print(title)

# MNG-246 Fix Detekt Config
prTitle = projectCode + '-' + ticketNumber + ' ' + title

os.system("git push -u origin " + branchName)
# os.system("gh pr create --draft --title " + prTitle)
