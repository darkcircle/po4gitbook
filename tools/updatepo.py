#!/usr/bin/python3
# -*- Mode: python -*-
# -*- coding: utf-8 -*-

import glob
import os


class UpdatePo:
    def __init__(self):
        self.popath = os.path.join(os.getcwd(), 'po')
        self.cmd_prefix = 'msgmerge -vU '
        self.cmd_pstfix = ' > /dev/null' #FIXME: to use os.devnull?
        
        self.potlist = []
        self.polist = []

    def create_cmd(self, pofile, potfile):
        argv = '{} {}'.format(pofile, potfile)
        return '{} {} {}'.format(self.cmd_prefix, argv, self.cmd_pstfix)

    def run(self):
        self.potlist = glob.glob(os.path.join(self.popath, '*.pot'))

        for pot in self.potlist:
            fn = os.path.split(pot)[-1].split('.')[0]
            fn += '.*.po'
            self.polist = glob.glob(os.path.join(self.popath, fn))

            for po in self.polist:
                print('Updating {} ...'.format(po))
                cmd = self.create_cmd(po, pot)
                print('$ {}'.format(cmd))
                os.system(cmd)


if __name__ == '__main__':
    u = UpdatePo()
    u.run()
