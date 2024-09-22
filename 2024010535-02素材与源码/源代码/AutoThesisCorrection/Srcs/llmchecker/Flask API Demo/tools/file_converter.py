from pypandoc.pandoc_download import download_pandoc
import os
import pypandoc
from config.appconfig import TEMP_PATH


def check_pandoc():
    try:
        pypandoc.get_pandoc_version()
    except OSError:
        download_pandoc()


def convertHtmlToDocx(html: str, outputfile):
    print("开始转换" + outputfile)
    # html写入临时文件
    with open(os.path.join(TEMP_PATH, "temp.html"), "w", encoding="utf-8") as f:
        f.write(html)
    pypandoc.convert_file(
        os.path.join(TEMP_PATH, "temp.html"), "docx", outputfile=outputfile
    )
