import os
import shutil


def remove_list(original_file_path, edit_id):
    original_file = open(original_file_path)
    read_flag = 1
    lines = ""

    while 1:
        s = original_file.readline()
        if s.replace("\n", "") == "<!-- start{0} -->".format(edit_id):
            read_flag = 0
            lines += "<!-- start{0} -->\n".format(edit_id)
        if s.replace("\n", "") == "<!-- end{0} -->".format(edit_id):   read_flag = 1
        if read_flag: lines += s
        if s == "": break

    with open(original_file_path, "w") as original_file:
        for line in lines:
            original_file.write(line)


def put_new_list(original_file_path, editted_info_path, edit_id):
    original_file = open(original_file_path)
    editted_info = open(editted_info_path)
    read_flag = 1
    lines = ""
    s = ""

    while 1:
        if read_flag:
            s = original_file.readline()
        if not read_flag:
            s = editted_info.readline()
            if s.replace("\n", "") == "<!-- end{0} -->".format(edit_id):
                read_flag = 1
                continue
        if s.replace("\n", "") == "<!-- start{0} -->".format(edit_id): read_flag = 0

        lines += s

        if s == "": break

    with open(original_file_path, "w") as f:
        for line in lines:
            f.write(line)


def icon_link_creator(splitted_list, temp_file_path):
    if splitted_list[3] == "": p_img_extension = "png"
    else:                      p_img_extension = splitted_list[3].replace("\"", "")
    if splitted_list[1] == "" and len(splitted_list[3]) <= 5: p_img_extension = "no_auto_img.lol"

    if len(p_img_extension) <= 5:
        if splitted_list[1].replace("/","") == splitted_list[1]:
            os.system("choco info \"{0}\" >> {1}".format(splitted_list[1], temp_file_path))
            choco_info_file = open(temp_file_path, "r+")
            choco_info_file.readline()
            choco_info = choco_info_file.readline()
            choco_info = choco_info.split()
            link = splitted_list[1] + "." + choco_info[1]
            choco_info_file.truncate(0)
            choco_info_file.close()
        else:
            link = splitted_list[1].replace("/",".")
        print(link)

        package_img = "<img src=\"https://community.chocolatey.org/content/packageimages/{0}.{1}\" width=\"16\" height=\"16\">".format(link, p_img_extension)
    else:
        if if_local_from: img_path = os.path.abspath(os.curdir).replace("\\list_editing", "") + "\\icons\\"  # on local pc    # "list editing" and "icons" should be variable
        else: img_path = "https://raw.githubusercontent.com/{0}/main/icons/".format(github_repo_link)
        package_img = "<img src=\"{0}{1}.{2}\" width=\"16\" height=\"16\">".format(img_path, splitted_list[0].replace(" ","_"), p_img_extension.replace("local.", ""))

    return package_img


def main_list_creator(list_path, temp_file_path):
    f = open(list_path)
    a = []
    final = ""
    form_check_opened = 0
    current_group = ""
    group_type = 0
    for i in f:
        if (len(i) > 6 and not (i[0:30] == "Displayed name,Choco pack name")) or i[0] == "#" or i[0] == "*" or i[0] == "%": a.append(i[:-1])
    for i in a:
        if i[0] == '*' or i[0] == '%':
            if form_check_opened == 1: final += "\n</div> \n\n"
            form_check_opened = 1
            current_group = i[1:-4] #Если буду расширять список, поменять здесь
            final += "<div class=\"form-check\">\n"
            final += "<input class=\"form-check-input\" type=\"checkbox\" name=\"category\" id=\"{0}\" value=\"{0}\">\n"\
                .format(current_group)
            final += "<label class=\"form-check-label\" for=\"{0}\"><h3>{0}</h3></label> <br>"\
                .format(current_group)
            if i[0] == '*': group_type = 1
            if i[0] == '%': group_type = 2
        else:
            splitted_list = i.split(",")
            if i[0] == "#":
                f = open(temp_file_path, "a")
                if (i.replace("\\", "") == "#") and (i.replace("\\", "") != i): f.write("<!-- end_comment -->\n")
                else:              f.write("<br>" + i[1:] + "\n")
                continue
            
            package_img = icon_link_creator(splitted_list, temp_file_path)

            package_link_html_opened = "<a href=\"https://community.chocolatey.org/packages/{0}\" target=\"_blank\">".format(
                splitted_list[1])
            choco_link_icon = "<img src=\"https://raw.githubusercontent.com/{0}/main/images/choco_icon.png\" width=\"16\" height=\"16\">".format(github_repo_link)

            winget_package_htmlopened = "<a href=\"https://wingetgui.com/apps?id={0}\" target=\"_blank\">".format(splitted_list[2])
            winget_icon = "<img src=\"https://raw.githubusercontent.com/{0}/main/images/WinGet_support.png\" width=\"16\" height=\"16\">".format(github_repo_link)

            extra_link_html_opened = "<a href=\"{0}\" target=\"_blank\">".format(splitted_list[4])
            link_icon = "<img src=\"https://raw.githubusercontent.com/{0}/main/images/url.svg\" width=\"16\" height=\"16\">".format(github_repo_link)

            if splitted_list[1].replace("/","") != splitted_list[1]:
                splitted_list[1] = splitted_list[1].split("/")[0] + " --version=" + splitted_list[1].split("/")[1]
                
            if package_img[-40:-25] == "no_auto_img.lol": package_img = ""
            if splitted_list[1] == "": choco_link_icon = ""
            if splitted_list[2] == "": winget_icon = ""
            if splitted_list[4] == "": link_icon = ""
            final += (
                "\n\n<input class=\"form-check-input\" type=\"checkbox\" name=\"app\" id=\",{1},{0},{2}\" value=\",{1},{0},{2}\">\n".format(
                    splitted_list[1], current_group, splitted_list[2]))
            if group_type == 1:
                final += "<label class=\"form-check-label\" for=\",{3},{1},{2}\">{4} {0} {5}{6}</a>{7}{8}</a>{9}{10}</a></label><br>".format(
                    splitted_list[0], splitted_list[1], splitted_list[2], current_group, package_img,
                    package_link_html_opened, choco_link_icon, winget_package_htmlopened, winget_icon, extra_link_html_opened, link_icon)
            if group_type == 2:
                final += "<label class=\"form-check-label\" for=\",{3},{1},{2}\">{5}{4}</a></label>".format(
                    splitted_list[0], splitted_list[1], splitted_list[2], current_group, package_img,
                    package_link_html_opened, )
                final += "<span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>"

    final += "\n</div> \n\n"
    final += "<!-- end -->\n"

    f = open(os.path.abspath(os.curdir) + "\\" + "html_formatted_list.txt", "w")
    f.write(final)
    f.close()


# Main
github_repo_link = "Deezbec/Chocolater-and-WinGeter"
html_file_name = "generator.html"
list_csv_name = "list.csv"
# Default_info
if_local_from = 0
generator_path = os.path.abspath(os.curdir) + "\\" + html_file_name
list_path = os.path.abspath(os.curdir) + "\\" + list_csv_name
temp_file_path = os.path.abspath(os.curdir) + "\\" + "temp_file.txt"
open(temp_file_path, "w").close()
shutil.copyfile(generator_path, generator_path.replace(html_file_name, html_file_name[:-5] + "_list_replaced" + html_file_name[-5:]))
generator_path = generator_path.replace(html_file_name, html_file_name[:-5] + "_list_replaced" + html_file_name[-5:])

input_text = input("Edit settings? (default: no): ")
if not (input_text == "") and not (input_text == "no"):
    if input("Get local images from? (github: \"\" - default; local: \"l\"): ") == "l":
       if_local_from = 0
    if input("Change github repo? current: \"{0}\"; default \"no\" ): ".format(github_repo_link)) != "":
       github_repo_link = input("Type your github repo link: ")



main_list_creator(list_path, temp_file_path)
remove_list(generator_path, "")  # remove list
remove_list(generator_path, "_comment")  # remove notes
put_new_list(generator_path, os.path.abspath(os.curdir) + "\\" + "html_formatted_list.txt", "")
put_new_list(generator_path, os.path.abspath(os.curdir) + "\\" + "temp_file.txt", "_comment")

os.remove(temp_file_path)
os.remove(os.path.abspath(os.curdir) + "\\" + "html_formatted_list.txt")

print("Completed!")
input()
