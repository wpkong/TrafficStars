# encoding: utf-8

if __name__ == '__main__':
	stars_f = open("stars.txt", "r")
	ban_list = open("bilibili_ban_list.xml", "w")

	ban_list.write("<filters>\n")
	for name in stars_f.readlines():
		ban_list.write("<item enabled=\"true\">t={}</item>\n".format(name.strip()))
	ban_list.write("</filters>")
	ban_list.close()
	stars_f.close()