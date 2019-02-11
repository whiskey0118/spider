from .getHtml import parseComment
from db.model import WeiboComment

def comment(url,wb_id):
    comment_list = list()
    for comment in parseComment(url):
        wb_comment = WeiboComment()
        try:
            cont = []
            first_author = True
            first_colon = True
            for content in comment.find(attrs={'class': 'WB_text'}).contents:
                if not content:
                    continue
                if content.name == 'a':
                    if first_author:
                        first_author = False
                        continue
                    else:
                        if content.text:
                            cont.append(content.text)

                elif content.name == 'img':
                    img_title = content.get('title', '')
                    cont.append(img_title)

                else:
                    if first_colon:
                        if content.find('：') == 0:
                            cont.append(content.replace('：', '', 1))
                            first_colon = False
                    else:
                        cont.append(content)
            wb_comment.comment_cont = ''.join(cont)
            wb_comment.comment_screen_name = comment.find(attrs={'class': 'WB_text'}).find('a').text
            wb_comment.comment_id = comment['comment_id']
            wb_comment.user_id = comment.find(attrs={'class': 'WB_text'}).find('a').get('usercard')[3:]
            wb_comment.create_time = comment.find(attrs={'class': 'WB_from S_txt2'}).text
            wb_comment.weibo_id = wb_id
        except Exception as e:
            print('解析评论失败，具体信息是{}'.format(e))
        else:
            comment_list.append(wb_comment)
    return comment_list

