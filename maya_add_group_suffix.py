from maya import cmds

obj_list = cmds.ls(sl=True)
if len(obj_list):
    for obj in obj_list:
        cmds.rename(obj, obj + '_low')
else:
    print('Select object(s)')
