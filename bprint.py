__author__ = 'Riju'
__email__ = 'mailmeonriju@gmail.com'


class Bprint:
    n_tab_prefix = 2
    BANNER_HEAD = '#################'
    BANNER_TAIL = '#################'

    def bprint(self, str_lst):
        for _ in range(self.n_tab_prefix):
            print('\t', end=" ")
        print(self.BANNER_HEAD)
        for line in str_lst:
            for _ in range(self.n_tab_prefix):
                print('\t#', end=" ")
            print('\t' + line + '\t#\n', end=" ")
        print('\n')
        for _ in range(self.n_tab_prefix):
            print('\t' + self.BANNER_HEAD)
        

if __name__ == '__main__':
    bprint_obj = Bprint()
    bprint_obj.bprint(['foo', 'bar123'])
