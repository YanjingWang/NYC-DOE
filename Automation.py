import os,glob,shutil
import base64
#import requests
import datetime
import time
from datetime import date
from ms_graph import generate_access_token
import win32com.client as win32
import subprocess
from pathlib import Path
import xlwings as xw
# from rpy2 import robjects


def createdir(path):
    # Check whether the specified path exists or not
    isExist = os.path.exists(path)
    if not isExist:   
        # Create a new directory because it does not exist 
        os.makedirs(path)
    else:
        return #'folder is created'

def rmfilesfromdir(dir):
    for files in os.listdir(dir):
        path = os.path.join(dir, files)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)

def rmonefile(path):
    isExist = os.path.exists(path)
    if isExist:   
        os.remove(path)
    else:
        return 

def copyonefile(src,dst):
    shutil.copy(src,dst)
    print('copying one file from {0} to {1} is compelte'.format(src,dst)) 

def copyallfiles(srcdir,dstdir):
    # shutil.copytree(srcdir,dstdir)
    files=os.listdir(srcdir)
 
    # iterating over all the files in
    # the source directory
    for fname in files:       
        # copying the files to the destination directory
        shutil.copy2(os.path.join(srcdir,fname), dstdir)
        print(fname)

def copyfiles(srcdir,dstdir):
    # shutil.copytree(srcdir,dstdir)
    files=os.listdir(srcdir)
 
    # iterating over all the files in
    # the source directory
    for fname in files:       
        # copying the files to the destination directory
        shutil.copyfile(os.path.join(srcdir,fname), dstdir)
        print(fname)

def openfiles(srcdir):
    # shutil.copytree(srcdir,dstdir)
    files=os.listdir(srcdir)
    for fname in files:
        if fname in ['Access Schools.xlsm','Bronx.xlsm','Brooklyn North.xlsm','Brooklyn South.xlsm','D75.xlsm','Manhattan.xlsm','Queens North.xlsm', 'Queens South.xlsm', 'Stanten Island.xlsm'] :
            fname = os.path.join(srcdir,fname)      
            os.startfile(fname)
            print(fname)
        else:
            return

def countfiles(srcdir):
    files=os.listdir(srcdir)
    count = 0
    for fname in files:
        count += 1
    print(count)
    return count

def printfiles(olddir,newdir):
    file_0822 = []
    files=os.listdir(olddir)
    for fname in files:
        file_0822.append(fname)
    file_0829 = []
    newfiles = os.listdir(newdir)
    for newfile in newfiles:
        file_0829.append(newfile)
    list_difference = []
    for element in file_0822:
        if element not in file_0829:
            list_difference.append(element)
    print(list_difference)

def copy_files_byfilename(src_folder, dest_folder, file_names):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    for file in os.listdir(src_folder):
        if file in file_names:
            src_file_path = os.path.join(src_folder, file)
            dest_file_path = os.path.join(dest_folder, file)
            shutil.copy2(src_file_path, dest_file_path)
            print(f"Copied {file} from {src_folder} to {dest_folder}")

def extract_first_six_chars(folder_path):
    file_prefixes = []
    for file in os.listdir(folder_path):
        file_prefixes.append(file[:6])
    return file_prefixes    



def RelatedServices():
    # Process 1 : Created PDFs for CSD and Charter schools
    # os.startfile(r'R:\All Central Offices\Special Ed Data\PA_Distribution_PDF')
    # os.startfile(r'R:\SEO Analytics\Reporting\Critical Processes\Related Services\SY22-23')
    # 1). create folders we need
    MDSY22_23 = "\\\\CENTRAL.NYCED.ORG\DoE$\SEO Analytics\Processing\Data Mart Files\Mandate_Distribution_SY22-23"
    int_pdfpath = 'C:\PA_Distribution_PDF'
    int_xlspath = 'C:\PA_Distribution_XLS'  # never been used
    int_charterpdf = 'C:\PA_DISTRIBUTION_PDF_Charter'
    int_charterxls = 'C:\PA_DISTRIBUTION_XLS_Charter'  # never been used
    CSD_Archive = 'R:\SEO Analytics\Processing\Data Mart Files\Archives\Backup_{0}'.format(date.today().strftime("%Y-%m-%d"))
    Charter_Archive = 'R:\SEO Analytics\Reporting\CharterArchive\{0}'.format(date.today().strftime("%Y%m%d"))
    dst_CSD_PDF = 'R:\All Central Offices\Special Ed Data\PA_Distribution_PDF'
    dst_CSD_XLS = 'R:\All Central Offices\Special Ed Data\PA_Distribution_XLS'
    shareCharter = 'R:\SEO Analytics\Share\Charter\{0}'.format(date.today().strftime("%Y%m%d"))
    mylocalXLSfolder = 'C:\Template'
    RSCompliance = 'R:\SEO Analytics\Share\Related Services\{0}'.format(date.today().strftime("%Y%m%d"))
    RSDashboardSharepoint = 'https://nycdoe.sharepoint.com/:f:/r/sites/RelatedServicesDashboard/Shared%20Documents/RS%20Compliance?csf=1&web=1&e=52Kaaq'

    createdir(int_pdfpath)
    createdir(int_xlspath)
    createdir(int_charterpdf)  
    createdir(int_charterxls)  
    createdir(CSD_Archive)
    createdir(Charter_Archive)  # really created?
    createdir(shareCharter)  # really created?
    createdir(mylocalXLSfolder)

    # 2.1): delete previous week XLS and PDF files 
    for f in os.listdir(dst_CSD_PDF):
        os.remove(os.path.join(dst_CSD_PDF, f))
        print(f)

    for file in os.scandir(dst_CSD_XLS):
        os.remove(file.path)
        print(file)

    rmfilesfromdir(int_pdfpath)
    rmfilesfromdir(int_xlspath)
    rmfilesfromdir(int_charterpdf)  # add to run guidance
    rmfilesfromdir(int_charterxls)  # add to run guidance
    rmfilesfromdir(mylocalXLSfolder)


    # 2.2) copy Mandate_Distribution_SY22-23 to your local C or D 
    copyonefile('\\\\CENTRAL.NYCED.ORG\DoE$\SEO Analytics\Processing\Data Mart Files\Mandate_Distribution_SY22-23\Mandate_Distribution_SY22-23.accdb', mylocalXLSfolder)
    os.startfile('C:\Template\Mandate_Distribution_SY22-23.accdb')
    time.sleep(60)
    now = datetime.datetime.now()
    print('Click Run and wait for 50 mins, now it is {0}'.format(now.strftime("%d/%B/%Y %H:%M:%S")))
    time.sleep(50*60)
    print('1598 files should be saved in C:\PA_Distribution_PDF and 271 files should saved in C:\PA_DISTRIBUTION_PDF_Charter.')

    print('Close Access file')
    time.sleep(60)
    rmonefile('C:\Template\Mandate_Distribution_SY22-23.accdb')
    time.sleep(10)
    #copy 1601 CSD files
    copyallfiles(int_pdfpath,dst_CSD_PDF)
    copyallfiles(int_pdfpath,CSD_Archive)
    print('copy pdf CSD files complete')

    # copy 275 chater files
    copyallfiles(int_charterpdf,shareCharter)
    copyallfiles(int_charterpdf,Charter_Archive)
    print('copy pdf charter files compelte')

def R_Process():
    #Process 2 : Create XLS Files for Charter and CSD schools
    MDSY22_23 = "\\\\CENTRAL.NYCED.ORG\DoE$\SEO Analytics\Processing\Data Mart Files\Mandate_Distribution_SY22-23"
    int_pdfpath = 'C:\PA_Distribution_PDF'
    int_xlspath = 'C:\PA_Distribution_XLS'  # never been used
    int_charterpdf = 'C:\PA_DISTRIBUTION_PDF_Charter'
    int_charterxls = 'C:\PA_DISTRIBUTION_XLS_Charter'  # never been used
    CSD_Archive = 'R:\SEO Analytics\Processing\Data Mart Files\Archives\Backup_{0}'.format(date.today().strftime("%Y-%m-%d"))
    Charter_Archive = 'R:\SEO Analytics\Reporting\CharterArchive\{0}'.format(date.today().strftime("%Y%m%d"))
    dst_CSD_PDF = 'R:\All Central Offices\Special Ed Data\PA_Distribution_PDF'
    dst_CSD_XLS = 'R:\All Central Offices\Special Ed Data\PA_Distribution_XLS'
    shareCharter = 'R:\SEO Analytics\Share\Charter\{0}'.format(date.today().strftime("%Y%m%d"))
    mylocalXLSfolder = 'C:\Template'
    RSCompliance = 'R:\SEO Analytics\Share\Related Services\{0}'.format(date.today().strftime("%Y%m%d"))
    RSDashboardSharepoint = 'https://nycdoe.sharepoint.com/:f:/r/sites/RelatedServicesDashboard/Shared%20Documents/RS%20Compliance?csf=1&web=1&e=52Kaaq'

    file1 = os.path.join(MDSY22_23,'RS_Reports_2022_2023.R')
    copyonefile(file1,mylocalXLSfolder)  
    file2 = os.path.join(MDSY22_23,'RS_Reports_2022_2023_Charter.R')
    copyonefile(file2,mylocalXLSfolder)
    newfile2 = os.path.join(mylocalXLSfolder,'RS_Reports_2022_2023_Charter.R')
    file3 = os.path.join(MDSY22_23,'RS_Template_new.xlsx')
    copyonefile(file3,mylocalXLSfolder)
    newfile3 = os.path.join(mylocalXLSfolder,'RS_Template_new.xlsx')
    file4 = os.path.join(MDSY22_23,'RS_Compliance_new.xlsx')
    copyonefile(file4,mylocalXLSfolder)
    newfile4 = os.path.join(mylocalXLSfolder,'RS_Compliance_new.xlsx')
    src_CSD ='\\\\CENTRAL.NYCED.ORG\DoE$\SEO Analytics\Reporting\Related Services\Output Files\SY 22-23\MandatedServices_{0}'.format(date.today().strftime("%Y%m%d"))
    src_Charter = '\\\\CENTRAL.NYCED.ORG\DoE$\SEO Analytics\Reporting\Related Services\Output Files\SY 22-23 Charter\MandatedServicesCharter_{0}'.format(date.today().strftime("%Y%m%d"))


    # file1 = os.path.join(mylocalXLSfolder,'RS_Reports_2022_2023.R')
    # os.startfile(file1)
    # print('Click Run and it takes 35 mins')
    # time.sleep(60*60)

    copyallfiles(src_CSD,dst_CSD_XLS)
    copyallfiles(dst_CSD_XLS,int_xlspath)  # copy PA_Distribution_XLS to archive?
    copyallfiles(dst_CSD_XLS,CSD_Archive)
    # copyallfiles(RSCompliance,RSDashboardSharepoint)

    # file2 = os.path.join(mylocalXLSfolder,'RS_Reports_2022_2023_Charter.R')
    # os.startfile(file2)
    # print('Click Run and it takes 5 mins')
    # time.sleep(5*60)
    # createdir(src_Charter)
    # createdir(Charter_Archive)  # really created?
    # createdir(shareCharter)  # really created?
    copyallfiles(src_Charter,shareCharter)
    copyallfiles(src_Charter,Charter_Archive)

def rerun_R():
    pdf_count = countfiles('R:\All Central Offices\Special Ed Data\PA_Distribution_PDF')
    xls_count = countfiles('R:\All Central Offices\Special Ed Data\PA_Distribution_XLS')
    src_CSD ='\\\\CENTRAL.NYCED.ORG\DoE$\SEO Analytics\Reporting\Related Services\Output Files\SY 22-23\MandatedServices_{0}'.format(date.today().strftime("%Y%m%d"))
    dst_CSD_XLS = 'R:\All Central Offices\Special Ed Data\PA_Distribution_XLS'
    int_xlspath = 'C:\PA_Distribution_XLS'
    CSD_Archive = 'R:\SEO Analytics\Processing\Data Mart Files\Archives\Backup_{0}'.format(date.today().strftime("%Y-%m-%d"))
    Charter_Archive = "R:\SEO Analytics\Reporting\CharterArchive\{0}".format(date.today().strftime("%Y%m%d"))
    CSD_Archive_count = countfiles(CSD_Archive)
    Charter_Archive_count = countfiles(Charter_Archive)
    # find the missing files
    folder1_path = 'R:\All Central Offices\Special Ed Data\PA_Distribution_PDF'
    folder2_path = 'R:\All Central Offices\Special Ed Data\PA_Distribution_XLS'
    folder1_prefixes = extract_first_six_chars(folder1_path)
    folder2_prefixes = extract_first_six_chars(folder2_path)
    # Find the different elements in the two lists
    folder1_unique_prefixes = list(
        set(folder1_prefixes) - set(folder2_prefixes))
    folder2_unique_prefixes = list(
        set(folder2_prefixes) - set(folder1_prefixes))
    print("Unique elements in folder PDF:", folder1_unique_prefixes)
    print("Unique elements in folder XLS:", folder2_unique_prefixes)
    if pdf_count > xls_count:
        print('PDF count is more than XLS count')
        print(CSD_Archive_count)
        print(Charter_Archive_count)
        # #clear R drive
        # rmfilesfromdir(src_CSD)
        # rmfilesfromdir(dst_CSD_XLS)
        # rmfilesfromdir(int_xlspath)
        # rmfilesfromdir(CSD_Archive)
        # R_Process()
    elif pdf_count == xls_count:
        print('PDF counts is equal to XLS Count')
    else:
        print('PDF has less files than XLS')
    
# def MandatedServices():
#     os.startfile(r'R:\SEO Analytics\Reporting\Critical Processes\Related Services\SY22-23')
#     #mylocalMandate = r'C:\Users\YWang36\Desktop\SESIS Mandated Services Report - AUTOMATED - SY22-23.xlsm'
#     file = 'R:\SEO Analytics\Processing\Data Mart Files\Templates\SESIS Mandated Services Report\SESIS Mandated Services Report - AUTOMATED - SY22-23.xlsm'
#     os.popen(file, 'r')
#     print("Click Enable Enable in the ribbon-->Developer tab: Click Macros button-->Click Run-->Wait for 4 mins")
#     time.sleep(5*60)

def MandatedServicesAuto():
    # specify path to your Excel file
    # excel_file_path = 'C:\Users\YWang36\Desktop\SESIS Mandated Services Report - AUTOMATED - SY22-23.xlsm'
    excel_file_path = 'R:\SEO Analytics\Processing\Data Mart Files\Templates\SESIS Mandated Services Report\SESIS Mandated Services Report - AUTOMATED - SY22-23.xlsm'
    # open the Excel file
    app = xw.App(visible=True)
    # os.startfile(excel_file_path)
    wb = app.books.open(excel_file_path)

    # specify the name of your macro
    macro_name = 'ThisWorkbook.Mandated_Services_Weekly_Processing'

    # run the macro
    app.api.Run(macro_name)

    # close the workbook and quit the app
    wb.close()
    app.quit()



def MandatedServices():
    path1 = Path(r'R:/SEO Analytics/Reporting/Critical Processes/Related Services/SY22-23')
    subprocess.run(['open', str(path1)])

    file_path = Path(r'R:/SEO Analytics/Processing/Data Mart Files/Templates/SESIS Mandated Services Report/SESIS Mandated Services Report - AUTOMATED - SY22-23.xlsm')
    subprocess.run(['open', str(file_path)])

    print("Click Enable Enable in the ribbon-->Developer tab: Click Macros button-->Click Run-->Wait for 4 mins")
    time.sleep(5*60)


def ms_send_outlook_email():
    # construct Outlook application instance
    olApp = win32.Dispatch('Outlook.Application')
    olNS = olApp.GetNameSpace('MAPI')

    # construct the email item object
    mailItem = olApp.CreateItem(0)
    mailItem.Subject = 'Mandated Services updates for {0}'.format(datetime.date.today())
    mailItem.BodyFormat = 1
    mailItem.Body = """Hi  All,\
    Updates at the Borough/City wide office (BCO) level have been updated to R:\Drive (R:\All Central Offices\Special Ed Data\PA SharePoint) and posted to SharePoint. \
    The above link is for sharing student level data.  If you are denied access, please log out of the network and then log back in. \
    * Please do not modify or store any personal files within any of our directories. We use that drive as a staging area to load and distribute student level data to various systems/people within the DOE.\
    Thanks,
    """
    # mailItem.To = 'YWang36@schools.nyc.gov' 
    # mailItem.Cc = 'gnutter@schools.nyc.gov;RMayilrajan@schools.nyc.gov' 
    mailItem.To = 'Van Biema Michael <MVanBiema@schools.nyc.gov>; Palladino Linette <LPalladino2@schools.nyc.gov>; Kaufman Helen <HKaufma@schools.nyc.gov>; Leo Maria <MLeo2@schools.nyc.gov>; \
    Elkayam Barry <BElkaya@schools.nyc.gov>; Shah Archana <AShah@schools.nyc.gov>; Stamm Charles <CStamm@schools.nyc.gov>; Leong Melanie <MLeong@schools.nyc.gov>; \
    Han Louise <LHan@schools.nyc.gov>; Silverman Joy <JSilverman8@schools.nyc.gov>'
    mailItem.Cc = 'Mayilrajan Rajamanickam <RMayilrajan@schools.nyc.gov>; ywang36@schools.nyc.gov; \
    Nutter Grace <GNutter@schools.nyc.gov>; Powers Alan <APowers3@schools.nyc.gov>' 

    # mailItem.Attachments.Add(os.path.join(os.getcwd(), 'fibonacci.py'))
    # mailItem.Attachments.Add(os.path.join(os.getcwd(), 'EmployeeClass.py'))

    mailItem.Display()

    mailItem.Save()
    mailItem.Send()


def rs_charter_send_outlook_email():
    # construct Outlook application instance
    olApp = win32.Dispatch('Outlook.Application')
    olNS = olApp.GetNameSpace('MAPI')

    # construct the email item object
    mailItem = olApp.CreateItem(0)
    mailItem.Subject = 'Weekly Charter Related Services Report {0}'.format(datetime.date.today())
    mailItem.BodyFormat = 1
    mailItem.Body = """Hello All, \
    Weekly charter Related Service reports are generated and saved at the following location: R:\SEO Analytics\Share\Charter\{0}
    """.format(date.today().strftime("%Y%m%d"))

    mailItem.To = 'Van Biema Michael <MVanBiema@schools.nyc.gov>; Delane Gurley Mia <MGurley@schools.nyc.gov>; Liu Mei <MLiu2@schools.nyc.gov>; \
    Thompson Karyn <KThompson7@schools.nyc.gov>; Sandi Mariama <MSandi@schools.nyc.gov>' 
    mailItem.Cc = 'Hammer John <JHammer4@schools.nyc.gov>; Daverin Rebecca <RDaverin2@schools.nyc.gov>; Powers Alan <APowers3@schools.nyc.gov>; \
    Mayilrajan Rajamanickam <RMayilrajan@schools.nyc.gov>; Grace Nutter <gnutter@schools.nyc.gov>; ywang36@schools.nyc.gov' 

    # mailItem.Attachments.Add(os.path.join(os.getcwd(), 'fibonacci.py'))
    # mailItem.Attachments.Add(os.path.join(os.getcwd(), 'EmployeeClass.py'))

    mailItem.Display()

    mailItem.Save()
    mailItem.Send()

def rs_compliace_send_outlook_email():
    # construct Outlook application instance
    olApp = win32.Dispatch('Outlook.Application')
    olNS = olApp.GetNameSpace('MAPI')

    # construct the email item object
    mailItem = olApp.CreateItem(0)
    mailItem.Subject = 'RS Dashboard and RS Compliance Report {0}'.format(
        datetime.date.today())
    # mailItem.BodyFormat = 1
    # mailItem.Body = """
    # Hi All,  \n
    # The Related Services Dashboard and RS Compliance Report are updated and posted to SharePoint. \n
    # Thank you!  
    # """.format(date.today().strftime("%Y%m%d"))
    # Here's the URL you want to link to
    sharepoint_url = 'https://nycdoe.sharepoint.com/sites/RelatedServicesDashboard/Shared%20Documents/Forms/AllItems.aspx?csf=1&web=1&e=52Kaaq&cid=0aa4e6f3%2D9bf2%2D4409%2Db358%2D30a2ef4843ef&FolderCTID=0x0120003896AEA985037F478C76713D8238A3C7&viewid=a94c67c5%2Dcfe7%2D4a86%2Da884%2D06fa1bc02cad'

    mailItem.HTMLBody = """
    <p>Hi All,</p>
    <p>The Related Services Dashboard and RS Compliance Report are updated and posted to <a href='{}'>SharePoint</a>.</p>
    <p>Thank you!</p>
    """.format(sharepoint_url, date.today().strftime("%Y%m%d"))
    mailItem.To = 'Yekaterina Magras <ymagras@schools.nyc.gov>;Corso Andie <ACorso6@schools.nyc.gov>;Gibson Shona <SGibson4@schools.nyc.gov>; Pandey Nick <npandey@schools.nyc.gov>; Magras Yekaterina <ymagras@schools.nyc.gov>; Avila Megan <mavila2@schools.nyc.gov>; Almeida Rebecca <ralmeida2@schools.nyc.gov>; Gottlieb Mandy <MGottlieb7@schools.nyc.gov>; Vidhi Dharia <vdharia@schools.nyc.gov>; Volpe Cen <CVolpe4@schools.nyc.gov>; Smith Samantha <SSmith110@schools.nyc.gov>; Dedaj Victoria <VDedaj@schools.nyc.gov>; Burnside Eric <EBurnside@schools.nyc.gov>; Odonnell Tricia (09X294) <TOdonnell2@schools.nyc.gov>; Mcfadden Melinda <MMcfadden9@schools.nyc.gov>; Rambaran Stephanie <SRambaran2@schools.nyc.gov>; Lipkowitz Michael <MLipkowitz@schools.nyc.gov>; Lewis Abbey <ALewis22@schools.nyc.gov>; Livingston Stacy <SLivingston2@schools.nyc.gov>; Bajana Sarah <SBajana@schools.nyc.gov>;Edwards Erin <EEdwards14@schools.nyc.gov>; Oppenheimer Daniella <doppenheimer3@schools.nyc.gov>; Demosthenes Aisha <ademosthenes@schools.nyc.gov>; Asaro Michelle <MAsaro3@schools.nyc.gov>;Galaise Jeffrey <JGalaise@schools.nyc.gov>; Johal Kamajit <KJohal@schools.nyc.gov>; Rivera Ivelisse <IRivera22@schools.nyc.gov>; Chasabenis Stamatis <SChasab@schools.nyc.gov>; Chan Lucilla <LChan10@schools.nyc.gov>;Lavergne Shakir <SLavergne@schools.nyc.gov>; Singleton Michelle <MSingle@schools.nyc.gov>; Sam Sasha <SSam2@schools.nyc.gov>; Miragliotta Carla <cmiragliotta@schools.nyc.gov>; Goodman Margaret <mgoodman3@schools.nyc.gov>; Smith Samantha <SSmith110@schools.nyc.gov>;Richardson Muriel <MRichardson3@schools.nyc.gov>;Alcantara Fatima <FAlcantara@schools.nyc.gov>; Alexander Carmen <CAlexan2@schools.nyc.gov>; Allen Michele <MAllen5@schools.nyc.gov>; \
    Antrobus Vann Abigail <AAntrobus@schools.nyc.gov>; Anzalone Christopher <CAnzalone2@schools.nyc.gov>; Aridas Cynthia <CAridas@schools.nyc.gov>;  \
    Bascoe Tanika <TBascoe@schools.nyc.gov>; Bastien-reneliq Stacy <SBastien@schools.nyc.gov>; Battista Michael <MBattis@schools.nyc.gov>; Ben-Moshe Yael <YBen-Moshe@schools.nyc.gov>; \
    Bernstein Edward <EBernstein6@schools.nyc.gov>; Berry Raquel <RBerry2@schools.nyc.gov>; Bethea Jenel <JBethea@schools.nyc.gov>; Bishop Andrea <ABishop3@schools.nyc.gov>; \
    Blitman Sara <SBlitman@schools.nyc.gov>; Bochbot Deborah <DBochbo@schools.nyc.gov>; Boone Cynthia <CBoone@schools.nyc.gov>; Brodsky Jacob <JBrodsky@schools.nyc.gov>; \
    Brown Harris Daria <dbrown6@schools.nyc.gov>; Brown Tiffany <TBrown70@schools.nyc.gov>; Brownstein Wendy <WBrownstein@schools.nyc.gov>; Burgos Evelyn <EBurgos2@schools.nyc.gov>; \
    Calliste Lesley Ann <LCallis@schools.nyc.gov>; Campos Yesenia <YCampos3@schools.nyc.gov>; Carrington Desiree <DCARRINGTON5@schools.nyc.gov>; Ceretti Michael <MCerett@schools.nyc.gov>; \
    Chall Brandon <BChall@schools.nyc.gov>; Chu Yuet <YChu@schools.nyc.gov>; Cirillo Catherine <CCirill@schools.nyc.gov>; Connelly Suzanne <SConnelly5@schools.nyc.gov>; \
    Cook Latipha <LCook8@schools.nyc.gov>; Cooper-Champion Tonya <disabled.TCooper2@schools.nyc.gov>; Cotler Debbie <DCotler@schools.nyc.gov>; Coursey Tara <TCoursey@schools.nyc.gov>; \
    Culbert Samantha <SCulbert@schools.nyc.gov>; Cummings Kisha <KCummings5@schools.nyc.gov>; Dandrea Kristyn <KDandrea@schools.nyc.gov>; Danker Jared <JDanker@schools.nyc.gov>; \
    Dapontes Stavroula <SDapontes@schools.nyc.gov>; Darrigo Dawn <DDarrigo@schools.nyc.gov>; Davis Mona <MDavis22@schools.nyc.gov>; De La Rosa Karen <KDeLaRosa@schools.nyc.gov>; \
    Degramont Darlyne <DDegramont@schools.nyc.gov>; Demosthenes Aisha <ADemosthenes@schools.nyc.gov>; Dicaro Jennifer <JDicaro@schools.nyc.gov>; Dickar Maryann <MDickar2@schools.nyc.gov>; \
    Difiore Joy <JDifiore3@schools.nyc.gov>; Dockery Smith Cecilia <CDockerySmith2@schools.nyc.gov>; Dorcelly Michael <MDorcelly@schools.nyc.gov>; Driesman Wendy <WDriesm@schools.nyc.gov>; \
    Edwards Ebony <disabled.EEdwards2@schools.nyc.gov>; Edwards Tabatha <TEdwards14@schools.nyc.gov>; Ehrenberg Debra <DEhrenberg@schools.nyc.gov>; Epstein Susan <SEpstein5@schools.nyc.gov>; \
    Escollies Iris <IEscoll@schools.nyc.gov>; Ewing Eric <EEwing@schools.nyc.gov>; Fabel Suzanne <SFabel@schools.nyc.gov>; Fenice Melissa <MFenice@schools.nyc.gov>; Fenoaltea Gina <GFenoaltea@schools.nyc.gov>; \
    Ferraiola Lisa <LFerrai@schools.nyc.gov>; Ferreira Giselle <GFerreira@schools.nyc.gov>; Figaro Jenny <JFigaro@schools.nyc.gov>; Foti Christina <CFoti@schools.nyc.gov>; Gallano Michael <MGallano2@schools.nyc.gov>; \
    Galvin Elizabeth <EGalvin4@schools.nyc.gov>; Gardner Sean <SGardner@schools.nyc.gov>; Gavryushenko Sergey <SGavryushenko@schools.nyc.gov>; George Monica <MGeorge@schools.nyc.gov>; Gold Seth <SGold6@schools.nyc.gov>; \
    Goldberg Caren <disabled.CGoldberg6@schools.nyc.gov>; Gonzalez Iris <IGonzal3@schools.nyc.gov>; Gonzalez Jorge <disabled.JGonzalez3@schools.nyc.gov>; Greene Shelley <disabled.SGreene8@schools.nyc.gov>; \
    Greenman Lauren <LGreenman2@schools.nyc.gov>; Groll Janice <JGroll@schools.nyc.gov>; Guercio Eileen <EGuercio@schools.nyc.gov>; Hammer John <JHammer4@schools.nyc.gov>; \
    Harris-pearson Tara <THarrispearson@schools.nyc.gov>; Henein Heba <HHenein@schools.nyc.gov>; Hinkley Michelle <MHinkley@schools.nyc.gov>; Hinton Sheila <SHinton2@schools.nyc.gov>; \
    Holbrook Daniel <DHolbrook2@schools.nyc.gov>; Hom David <DHom@schools.nyc.gov>; Hughes Rose Marie <RHughes4@schools.nyc.gov>; Inzerelli Antonietta <AInzerelli@schools.nyc.gov>; \
    Jean Claude Richard <RJeanCl@schools.nyc.gov>; Jean Guyline <JGuyline@schools.nyc.gov>; Jenkins Jacqueline <JJenkins8@schools.nyc.gov>; \
    Jennings Gregory <GJennin@schools.nyc.gov>; Johal Kamajit <KJohal@schools.nyc.gov>; Johnson Daly Veronica <VJohnsonDaly@schools.nyc.gov>; Jones Juliette <JJones42@schools.nyc.gov>; \
    Jones Kivel <KJones46@schools.nyc.gov>; Joshi Manasi <MJoshi5@schools.nyc.gov>; Kagimbi Loise <LKagimbi2@schools.nyc.gov>; Karty Alison <AKarty@schools.nyc.gov>; Katz Chana <CKatz6@schools.nyc.gov>; \
    Kaufman Helen <HKaufma@schools.nyc.gov>; Kessler Rizzo Jessica <JKessler6@schools.nyc.gov>; Khan Ahsan <disabled.AKhan37@schools.nyc.gov>; Kim Andrea <AKim14@schools.nyc.gov>; Kim Virginia <disabled.VKim@schools.nyc.gov>; \
    King Kathleen <KKing@schools.nyc.gov>; Kip Carlotta <disabled.CKip@schools.nyc.gov>; Kish Lauren <LKish@schools.nyc.gov>; Konig Phillip <PKonig@schools.nyc.gov>; Kopiec Robert <RKopiec@schools.nyc.gov>; \
    Korman Alice <AKorman@schools.nyc.gov>; Kostel Matt (750000) <MKostel@schools.nyc.gov>; Krayets Alexandra <AKrayets@schools.nyc.gov>; Kutner Hallie <HKutner@schools.nyc.gov>; Gaynor Charmaine <CGaynor@schools.nyc.gov>; \
    LaBarbera Judith <JLaBarbera2@schools.nyc.gov>; Lantzounis Alexia <ALantzounis@schools.nyc.gov>; Leong Melanie <MLeong@schools.nyc.gov>; Levine Bambi <disabled.BLevine7@schools.nyc.gov>; Levitt Luisa <LLevitt@schools.nyc.gov>; \
    Lieberman Justin <JLieberman5@schools.nyc.gov>; Lin Lisa <CLin2@schools.nyc.gov>; Louissaint Ketler <KLouiss@schools.nyc.gov>; Lubalin Stephanie <SLubalin@schools.nyc.gov>; Mahamed Saudia <SMahamed@schools.nyc.gov>; Mandel Betsy <BMandel6@schools.nyc.gov>;\
    Martin Glenn <GMartin6@schools.nyc.gov>; Marupaka Phani Bhushan <PMarupaka@schools.nyc.gov>; Marzan Kelly <KMarzan@schools.nyc.gov>; Mason Theodore <tmason@schools.nyc.gov>; Mayilrajan Rajamanickam <RMayilrajan@schools.nyc.gov>; \
    Mcgill Stephanie <SMcGill2@schools.nyc.gov>; Mckenzie Royelle <RMckenzie@schools.nyc.gov>; Mcloughlin Lori Ann <LMcloughlin2@schools.nyc.gov>; Mcnulty Contessa <CMcnulty@schools.nyc.gov>; Miller Abby <AMiller14@schools.nyc.gov>; \
    Miller Michele <MMiller26@schools.nyc.gov>; Mills Mona <disabled.MMills2@schools.nyc.gov>; Mintzer Lisa <LMintze@schools.nyc.gov>; Mitchell Nicole <NMitchell4@schools.nyc.gov>; Monaco Emma <EMonaco@schools.nyc.gov>; Morales Marina <MMorales15@schools.nyc.gov>; \
    Mosquera-Valeri Sandra <SMosquera@schools.nyc.gov>; Motola Phyllis <PMotola@schools.nyc.gov>; Mulcahy Kathleen <KMulcahy@schools.nyc.gov>; Mullen Smith Aileen <AMullen4@schools.nyc.gov>; Navarette Luisa <LNavarette@schools.nyc.gov>; \
    Navarrete Cristina <CNavarrete@schools.nyc.gov>; Nicome Natasha <NNicome@schools.nyc.gov>; Nutter Grace <GNutter@schools.nyc.gov>; Ocharsky Adam <AOcharsky@schools.nyc.gov>; Ogir Crystal <COgir@schools.nyc.gov>; Ojeda Lucy <LOjeda@schools.nyc.gov>; \
    Oleary-Toro Kristen (CFN Cluster 6) <KOleary@schools.nyc.gov>; Onwumere Dora <DOnwumere2@schools.nyc.gov>; Ortiz Jackeline <JOrtiz50@schools.nyc.gov>; Patterson Thomas <TPatterson4@schools.nyc.gov>; Pearson Jamie <JPearson5@schools.nyc.gov>; \
    Perez Ferdinand Blanca <BPerez4@schools.nyc.gov>; Perez Jerry <JPerez42@schools.nyc.gov>; Piccininno Lori <LPiccin@schools.nyc.gov>; Plutchok Malka <MPlutch@schools.nyc.gov>; Polomsky Martin <MPolomsky@schools.nyc.gov>; Powers Alan <APowers3@schools.nyc.gov>; \
    Prowell Sean <SProwell@schools.nyc.gov>; Pupello Lois <LPupell@schools.nyc.gov>; Raguse Betsy <BRaguse@schools.nyc.gov>; Ramirez William <WRamirez@schools.nyc.gov>; Ramones Kimberly <KRamones@schools.nyc.gov>; Ramos Marissa <MRamos60@schools.nyc.gov>; \
    Reese Stephen <SReese2@schools.nyc.gov>; Regan Cori <CRegan@schools.nyc.gov>; Restivo Christopher (75R025) <CRestiv@schools.nyc.gov>; Riccobono Joseph <JRiccobono@schools.nyc.gov>; Robinson Denise <DRobins5@schools.nyc.gov>; Robles Michelle <MRobles3@schools.nyc.gov>; \
    Rodriguez Luisa <disabled.LRodriguez133@schools.nyc.gov>; Rosenberg Aron <ARosenb6@schools.nyc.gov>; Rotenberg Sheri <SRotenberg@schools.nyc.gov>; Rozovskaya Liana <LRozovskaya@schools.nyc.gov>; Rubino Charles <CRubino3@schools.nyc.gov>; \
    Rupnarain Bebi <BRupnar@schools.nyc.gov>; Sackris Brent <BSackris@schools.nyc.gov>; Safyan Diana <DSafyan@schools.nyc.gov>; Sanchez Suzanne <SSanchez8@schools.nyc.gov>; Santos Lais <LSantos8@schools.nyc.gov>; Sattar Maryam <MSattar2@schools.nyc.gov>; \
    Savarin Madeline <MSavarin2@schools.nyc.gov>; Schmitt Peter <PSchmitt@schools.nyc.gov>; Schwartz Devin <DSchwartz9@schools.nyc.gov>; Sealy Marita <disabled.MSealy@schools.nyc.gov>; Segev Shelly <SSegev@schools.nyc.gov>; Seidman Steven <SSeidman4@schools.nyc.gov>; \
    Shats Aleksey <AShats@schools.nyc.gov>; Sippy Sujeeta <SSippy@schools.nyc.gov>; Song Mi Jung Judile <MSong2@schools.nyc.gov>; Stamm Charles <CStamm@schools.nyc.gov>; Stanislas Martina <MStanis@schools.nyc.gov>; Stefkovich Donna <DStefkovich@schools.nyc.gov>; \
    Sylvester Karen <KSylvester4@schools.nyc.gov>; Taharally Christophe <CTaharally@schools.nyc.gov>; Tarnarider Nataly <NTarnarider@schools.nyc.gov>; Tenenbaum Batya <BTenenbaum@schools.nyc.gov>; Terzulli Raffaella <RTerzul@schools.nyc.gov>; Testani Kristin <KTestani@schools.nyc.gov>; \
    Thomas Carin <CThomas82@schools.nyc.gov>; Tomeo Jessica <disabled.JTomeo2@schools.nyc.gov>; Tomeo Julia <JTomeo@schools.nyc.gov>; Torres Angela <ATorres21@schools.nyc.gov>; Trivedi Sejal <STrivedi@schools.nyc.gov>; Tsirulnikov Zoya <ZTsirulnikov@schools.nyc.gov>; \
    Tumelty Margaret <MTumelty@schools.nyc.gov>; Valentine Valerie <VValentine@schools.nyc.gov>; Van Biema Michael <MVanBiema@schools.nyc.gov>; Van Holt Lisa <LVanHolt@schools.nyc.gov>; VanZetta Christine <CVanzet@schools.nyc.gov>; Vasquez Daliz <DVasquez3@schools.nyc.gov>; \
    Walker Karin <KWalker@schools.nyc.gov>; Wang Yanjing <YWang36@schools.nyc.gov>; Ware-Malleuve Kismet <KWareMalleuve@schools.nyc.gov>; Weaver Joseph <JWeaver2@schools.nyc.gov>; Wedderburn Simpson Barbara <BWedder@schools.nyc.gov>; Weiss Yael <YWeiss@schools.nyc.gov>;\
    Whitfield Buffie <BWhitfield2@schools.nyc.gov>; Williams Angela <AWillia6@schools.nyc.gov>; Williams Audrey <AWillia7@schools.nyc.gov>; Williams Donnette <DWilliams41@schools.nyc.gov>; Wilson Marion <MWilson11@schools.nyc.gov>; Wisker Maria <MWisker@schools.nyc.gov>; \
    Yakubov Nathan <NYakubov@schools.nyc.gov>; Young Darnell <DYoung10@schools.nyc.gov>; Zamore Dena <DZamore@schools.nyc.gov>; Zarate Alexandra <AZarate@schools.nyc.gov>; Zeltser Michelle <MZeltser@schools.nyc.gov>; Zervoulei Devito Kimberly <KZervouleiDevito@schools.nyc.gov>; \
    Floyd Nichole (75X811) <NFloyd@schools.nyc.gov>; Chang Tiffany <TChang2@schools.nyc.gov>; Mintzer Lisa <LMintze@schools.nyc.gov>; Ehrenberg Debra <DEhrenberg@schools.nyc.gov>; MMcCall@schools.nyc.gov;'
    mailItem.Display()

    mailItem.Save()
    mailItem.Send()



def archive_rs_borough():
    source_folder = '\\\\CENTRAL.NYCED.ORG\DoE$\SEO Analytics\Reporting\RS Dashboard\Weekly RS Dashboard'
    destination_folder = 'R:\SEO Analytics\Reporting\RS Dashboard\Weekly RS Dashboard Archive\{0}'.format(
        date.today().strftime("%Y%m%d"))
    file_names_to_copy = ['Access Schools.xlsx', 'Bronx.xlsx', 'Brooklyn North.xlsx', 'Brooklyn South.xlsx', 'Citywide.xlsx',
                          'Citywide RS Powerpoint.pptm', 'D75.xlsx', 'Manhattan.xlsx', 'Queens North.xlsx', 'Queens South.xlsx', 'Stanten Island.xlsx']
    copy_files_byfilename(source_folder, destination_folder, file_names_to_copy)

if __name__ == '__main__':
    # RelatedServices()
    # R_Process()
    # rerun_R()
    rs_charter_send_outlook_email()
    # MandatedServices()
    ms_send_outlook_email()
    rs_compliace_send_outlook_email()
    # openfiles('R:\SEO Analytics\Reporting\RS Dashboard\Weekly RS Dashboard')
    archive_rs_borough()


