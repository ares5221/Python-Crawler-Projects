#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os
from docx import Document
from win32com import client as wc



def create_classifer_files(key):
    print('kaishixiazai')
    base_dir = './../data_v2/target/'
    curr_dir = os.path.join(base_dir, key)
    if not os.path.exists(curr_dir):
        os.makedirs(curr_dir)
    if not os.path.exists(os.path.join(curr_dir, '试题')):
        os.makedirs(os.path.join(curr_dir, '试题'))
    if not os.path.exists(os.path.join(curr_dir, '资料')):
        os.makedirs(os.path.join(curr_dir, '资料'))
    if not os.path.exists(os.path.join(curr_dir, '课件')):
        os.makedirs(os.path.join(curr_dir, '课件'))


def text_content_analysis(key):
    create_classifer_files(key)
    base_dir = './../data_v2/source'
    curr_dir = base_dir + '/' + key
    for file_item in os.listdir(curr_dir):
        curr_file_name = os.path.join(curr_dir, file_item)
        # print(curr_file_name)
        # todo
        # https: // www.jianshu.com / p / 056e94
        # ca301e
        if file_item[-5:] == '.docx':
            phrase_docx(curr_file_name)
        if file_item[-4:] == '.doc':
            phrase_doc(curr_file_name)
        if file_item[-4:] == '.txt':
            pass
        if file_item[-4:] == '.pdf':
            pass
        if file_item[-4:] == '.ppt':
            pass



def phrase_doc(file_path):
    print(file_path)
    ab_path = r'G:\Download\AutoCrowerByKeyWords\data_v2\source\光合作用'
    sp = os.path.split(file_path)
    # abs_path = sp[0]
    file_name = sp[1]
    # ss = abs_path + file_name
    file_path = os.path.join(ab_path, file_name)
    # print(abs_path)
    # print(file_name)
    word = wc.Dispatch('Word.Application')
    doc = word.Documents.Open(file_path)
    for para in doc.paragraphs:
        print(para.Range.Text)
    # newname = save_dir + '/' + fname[:-4] + '.docx'
    # # print(curr_file_name)
    # # print(newname)
    # # print(fname,'ssssss')
    # doc.SaveAs(newname, 16)
    doc.Close()


def phrase_docx(file_path):
    sp = os.path.split(file_path)
    abs_path = sp[0]
    file_name = sp[1]
    document = Document(file_path)  # 打开docx文件
    full_text = []
    for paragraph in document.paragraphs:
        full_text.append(paragraph.text)
    # print(file_name,full_text)
    if '试题' in file_name or ('答题表' in full_text and '班级' in full_text and '姓名' in full_text):
        return '试题'
    if '练习' in file_name or '同步练习' in full_text or '基础练习' in full_text or '资料' in file_name:
        return '资料'
    if '课件' in file_name or '笔记' in full_text or '专题' in file_name or '笔记' in file_name:
        return '课件'



def change_doc2docx(file_path):
    word = wc.Dispatch('Word.Application')
    doc = word.Documents.Open(file_path)
    newname = save_dir + '/' + fname[:-4] + '.docx'
    # print(curr_file_name)
    # print(newname)
    # print(fname,'ssssss')
    doc.SaveAs(newname, 16)
    doc.Close()



if __name__=='__main__':
    key = '光合作用'
    text_content_analysis(key)