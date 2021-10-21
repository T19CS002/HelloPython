'''
Created on 2021/10/15

@author: csuser
'''

import random

#0=グー、1=チョキ、2=パー
aNum = random.randint(0,2)
bNum = random.randint(0,2)

#出した手の判定
if aNum == 0:
    aHand = 'グー'
elif aNum == 1:
    aHand = 'チョキ'
else:
    aHand = 'パー'

if bNum == 0:
    bHand = 'グー'
elif bNum == 1:
    bHand = 'チョキ'
else:
    bHand = 'パー'

#勝敗判定    
if aNum == bNum:
    result = '引き分け'
elif aNum == 0 and bNum == 1 or aNum == 1 and bNum == 2 or aNum == 2 and bNum == 0:
    result = 'Aの勝ち'
else:
    result = 'Bの勝ち'
    
print("Aの手：" + aHand + " v.s. Bの手：" + bHand + " → " + result)




