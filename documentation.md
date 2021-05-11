# Diary Viewer Documentaion

### 1. Download the transcription uploaded online
- Use [this link](https://depts.washington.edu/newbook/data/JMS/jms_idx.html) to find the diary that you want to transcribe.
- When you have located the diary you want, right click and select “View page source”, copy all, and save it as a .txt file named "input". 

### 2. Find all the image urls
- Use [this link](https://digitalcollections.lib.washington.edu/digital/collection/iraqdiaries/search) (UW University Libraries Digital Collection), navigate to the diary you want, and look at the first image. 
- Right click the image to find its image address, it should look something like this: "https://i.imgur.com/XgzeckH.jpg"
- Next, find the img url of the last page in the diary. 
- Remember the start and end page number in the urls for the diary.

### 3. Run the python file for the transcription
- Download and open the python file named "DV file-editor".
- Change the variable "diary" to the diary number which you are working on right now.
- Change the variables "startpage" and "endpage" to the corresponding numbers you got from the last step.
- Run the python file! (remember to keep the input and python editor file in the same directory!)
- There should be two output files with name "sychronized" and "asynchronized" corresponding to the two versions of the diary viewer.

### 4. Upload to Wordpress
- Download the css and javascript file.
- Open wordpress and start a new page.
- Type down {{CODE}}, {{CODEStyle}}, and {{CODEScript}} in three different lines.
- In Custom field, add three fields with names CODE, CODEStyle, and CODEScript.
- Copy and paste the corresponding page contents into the fields.

### 5. Save and preview
- Click "save draft" on the top left corner of your screen.
- Click "preview" to check on the draft you just created.