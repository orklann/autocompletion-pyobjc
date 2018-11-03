import inspect
import Cocoa
import Quartz
import Foundation

lookup = dict()

def listModule(module):
    for i in dir(module):
        if not lookup.get(i):
            print(i)
            lookup.setdefault(i, True)
        t = getattr(module, i)
        if inspect.isclass(t):
            listClass(t)

def listClass(c):
    for i in dir(c):
        if not lookup.get(i):
            print(i)
            lookup.setdefault(i, True)

listModule(Foundation)
listModule(Cocoa)
listModule(Quartz)
