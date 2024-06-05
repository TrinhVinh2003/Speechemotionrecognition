import os 
from lib.ham_ho_tro import xoa_file, xoa_thu_muc, tao_thu_muc , xoa
from lib.info import name, member



try:
    xoa_thu_muc('__pycache__')
except:
    pass
try:
    xoa_thu_muc('lib/__pycache__')
except:
    pass

cwd = os.getcwd()

if 'speech emotion recognition' in cwd:
    if member(name()):
        path_share = os.path.join(cwd, 'share')
        if os.path.isdir(path_share):
            raise Exception('Thư mục share đã tồn tại, bạn cần xóa thư mục này đi và chạy lại để tránh lỗi đồng bộ')
        tao_thu_muc("share")
        os.chdir('share')
        os.system('git init')
        os.system('git branch -M main')
        # os.system('git remote add share ')
        os.system('git pull share main')
else:
    raise Exception('open sai thư mục. vui lòng open thư mục speech emotion recognition')


os.chdir(cwd)
os.system('pip install -r storage/library.txt')

xoa_file('lib/info.py')

xoa()