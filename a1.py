# -- coding: UTF-8 --
import os

def test1():
	f2=open("1_invite_uid.txt","w+")
	with open('user1.txt', 'r') as f1:
		for i in f1:
			#print "i is: ",i,
			f2.write("select count(*) from fa_user where invite_uid=%s\n"%i)
	f2.close()
	f1.close()


def test2(uid,invite_num,src_score,score):
	after_score=src_score+score
	f_name="3_sql_user_score_log_%s.txt"%uid
	print(f_name)
	f3=open(f_name,"w+")
	for i in range(invite_num):
		f3.write('INSERT INTO fa_user_score_log (uid, score, flag, before, after, addtime, remark, type) VALUES (%s, %s, +, %s, %s, 1531312626, 邀请好友注册得积分, offline);\n'%(uid,score,src_score,after_score))
		src_score=after_score
		after_score+=score
	f3.close()
	del f_name

def test3(invite_num,src_score,score):
	f1=open("2_test2_fun_tmp.txt","w+")
	with open('u.txt', 'r') as f2:
	# with open('user1.txt', 'r') as f2:
		for i in f2:
			print i,
			f1.write("test2(%s,%s,%s,%s)\n"%(i.strip("\n"),invite_num,src_score,score))
			#test2(i.strip("\n"),invite_num,src_score,score)
	f2.close()
	f1.close()

#生成sql语句，查询每一个邀请者邀请好友人数
test1()

#执行1_invite_uid.txt中的sql语句，查询每个人邀请的人数 invite_num
#uid = 723
src_score = 0
score = 3
# invite_num,src_score,score
invite_num = 3 #修改为实际值
test3(invite_num,src_score,score) #modify invite_num to

#copy tmp.txt file to this place
#uid，invite_num,src_score,score
#

#将3_开头的文件内容，在数据库中执行，为用户端添加积分明细

#修改数据库，修改剩余积分
#修改数据库，修改已获得总积分


