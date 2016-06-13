#!/usr/bin/env python
# coding=utf-8


class Skills:

    def __init__(self, **kwargs):
        self.skills = set(kwargs.values())

    def __repr__(self):
        return 'Skills: {}'.format(','.join(i for i in self.skills))

    def __len__(self):
        return len(self.skills)

    def learn(self, new_skill):
        print '新技能 {} get'.format(new_skill)
        return self.skills.add(new_skill)

    def forget(self, old_skill):
        return self.skills.discard(old_skill)

if __name__ == '__main__':
    I = Skills(a='swim', b='basketball')
    print I
    I.learn(new_skill='python')
    print I
    print len(I)
