![Chocolater](https://raw.githubusercontent.com/mariosemes/Chocolater/main/images/simple-logo.jpg "Chocolater")
#### App Install Tool

[![CLICK TO VISIT GENERATO with Deezbec's progs](https://img.shields.io/badge/Click_To_Visit_Generator-blue.svg?style=for-the-badge)](https://raw.githack.com/Deezbec/Chocolater-and-WinGeter/main/generator.html)
Deezbec's list

[![CLICK TO VISIT GENERATO with Mariosemes's progs](https://img.shields.io/badge/Click_To_Visit_Generator-blue.svg?style=for-the-badge)](https://raw.githack.com/Deezbec/Chocolater-and-WinGeter/main/additional%20files%20and%20progs/generator_mariosemes.html)
Mariosemes's list

Basically it is [Chocolater](https://github.com/mariosemes/Chocolater) by [Mariosemes](https://github.com/mariosemes) with new features:

1) Simple creation of your own list
2) Icons for programs are automatically got from chocolatey's program package page
3) WinGet support
4) "Select all" from group<br><br>
Remark about "Select all from group" check box: <br> While it is active checking boxes of entryes of the selected group will remove them from selection

------------
## Want to create your own list?

1) Download the source code
2) Edit "list.csv" (I personally do this with VS code's [edit CSV](https://marketplace.visualstudio.com/items?itemName=janisdd.vscode-edit-csv) extension)<br><br>  

|Displayed name|Choco pack name|WinGet pack name|icon file format or <local.format>|Extra link|  
|--------------|---------------|----------------|----------------------------------|----------|  
|Brave|brave|BraveSoftware.BraveBrowser|svg|https://brave.com/|  
|Python|python/3.9.5|Python.Python|svg||
|Totalcommander|totalcommander|Ghisler.TotalCommander|||
|Everything|everything||||
|win10 tweaker|||local.png||
|ISLC - standby list cleaner|||||

Result:  
<label class="form-check-label" for=",Browser,brave,BraveSoftware.BraveBrowser"><img src="https://community.chocolatey.org/content/packageimages/brave.1.46.153.svg" width="16" height="16"> Brave <a href="https://community.chocolatey.org/packages/brave" target="_blank"><img src="https://raw.githubusercontent.com/Deezbec/Chocolater-and-WinGeter/main/images/choco_icon.png" width="16" height="16"></a><a href="https://wingetgui.com/apps?id=BraveSoftware.BraveBrowser" target="_blank"><img src="https://raw.githubusercontent.com/Deezbec/Chocolater-and-WinGeter/main/images/WinGet_support.png" width="16" height="16"></a><a href="https://brave.com/" target="_blank"><img src="https://raw.githubusercontent.com/Deezbec/Chocolater-and-WinGeter/main/images/url.svg" width="16" height="16"></a></label><br>
<label class="form-check-label" for=",Browser,python --version=3.9.5,Python.Python"><img src="https://community.chocolatey.org/content/packageimages/python.3.9.5.svg" width="16" height="16"> Python <a href="https://community.chocolatey.org/packages/python/3.9.5" target="_blank"><img src="https://raw.githubusercontent.com/Deezbec/Chocolater-and-WinGeter/main/images/choco_icon.png" width="16" height="16"></a><a href="https://wingetgui.com/apps?id=Python.Python" target="_blank"><img src="https://raw.githubusercontent.com/Deezbec/Chocolater-and-WinGeter/main/images/WinGet_support.png" width="16" height="16"></a><a href="" target="_blank"></a></label><br>
<label class="form-check-label" for=",Browser,totalcommander,Ghisler.TotalCommander"><img src="https://community.chocolatey.org/content/packageimages/totalcommander.10.51.png" width="16" height="16"> Totalcommander <a href="https://community.chocolatey.org/packages/totalcommander" target="_blank"><img src="https://raw.githubusercontent.com/Deezbec/Chocolater-and-WinGeter/main/images/choco_icon.png" width="16" height="16"></a><a href="https://wingetgui.com/apps?id=Ghisler.TotalCommander" target="_blank"><img src="https://raw.githubusercontent.com/Deezbec/Chocolater-and-WinGeter/main/images/WinGet_support.png" width="16" height="16"></a><a href="" target="_blank"></a></label><br>
<label class="form-check-label" for=",Browser,everything,"><img src="https://community.chocolatey.org/content/packageimages/everything.1.4.11022.png" width="16" height="16"> Everything <a href="https://community.chocolatey.org/packages/everything" target="_blank"><img src="https://raw.githubusercontent.com/Deezbec/Chocolater-and-WinGeter/main/images/choco_icon.png" width="16" height="16"></a><a href="https://wingetgui.com/apps?id=" target="_blank"></a><a href="" target="_blank"></a></label><br>
<label class="form-check-label" for=",Browser,,"><img src="https://raw.githubusercontent.com/Deezbec/Chocolater-and-WinGeter/main/icons/win10_tweaker.png" width="16" height="16"> win10 tweaker <a href="https://community.chocolatey.org/packages/" target="_blank"></a><a href="https://wingetgui.com/apps?id=" target="_blank"></a><a href="" target="_blank"></a></label><br>
<label class="form-check-label" for=",Browser,,"> ISLC - standby list cleaner <a href="https://community.chocolatey.org/packages/" target="_blank"></a><a href="https://wingetgui.com/apps?id=" target="_blank"></a><a href="" target="_blank"></a></label><br>






Columns stand for:  
1st - Displayed package name  
2nd - Chocolatey package name (its also used to get icons)  
if you want to set specific version, add "/<versionNumber>", example "python/3.9.5"  
3rd - WinGet pack name (optional)  
4th - What is icon on chocolatey package page extension (default - png)  
      Or what is extension of local icon. example - "local.{format}"  
      In program "local" is changed for displayed package name, all the " " are changed for "_"  
      example: win10_tweaker.png  
5th - Extra link, mainly for programs with no available packages <br><br>
Rows:  
Can be devided to 3 categories:<br><br>
1st -  Group  
Groups can start with:  "\*","%"  
"\*" - standart list  
"%" - standart compact list. Can be used to create pack's of programs  <br><br>
2nd - Entry  
Just Enter all the needed information for the entry<br><br>
3rd - Comments  
They should be place on the bottom of list.csv file  
Each line have to be started with "#"  
Comment section ends with: "#\\\\\\" KEEP IT EVEN IF YOU DONT NEED COMMENTS

3) Run "Create & replace list.py"  
For some reason I can't run it without IDE, no idea how to fix  
That's why I recommend you to launch it in VS code with python or any other IDE  
if everything is ok, you will see your programs names with the latest version found on Chocolatey  
Program should end with "Completed!"  
If you have any problems, feel free to msg me on discord Deezbec#2094 or create a ticket on github  

------------
## Development notes

### Feature ideas:  
1) hover program summery;  


### Known issues:  
1) if there is no "#\\\\\\" in the end of .csv file, it does not work properly 
2) Some icons got from chocolatey website are not stable
3) I guess I gotta download icons, cause I hardly ever update my list




------------
### License
This script is under the [GNU General Public License v3.0](https://github.com/mariosemes/Chocolater/blob/main/LICENSE "GNU General Public License v3.0") License.
