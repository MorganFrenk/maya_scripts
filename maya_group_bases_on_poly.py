from maya import cmds

obj_list = cmds.ls(sl=True)
if obj_list:
  objs_polys_count = [(cmds.polyEvaluate(obj, vertex=True), obj) for obj in obj_list]
	min_polys_obj = min(objs_polys_count)
	for obj in obj_list:
    pref = '_low' if obj == min_polys_obj[1] else '_high'
		cmds.rename(obj, min_polys_obj[1] + pref)
else:
	print('Select object(s)')
