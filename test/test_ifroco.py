from utils import *


class TSF(VCTestCase):

    for test_name in [
        'test_ifroco_curves',
        'test_ifroco_map',
        ]:
        exec(method_template.format(test_name))
        
        
if __name__ == '__main__':
    unittest.main()
