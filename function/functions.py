def get_tree(queryset,pid=0,level=1):		
	tree = []
	for node in queryset:
		if node['pid'] == pid :
			node['level'] = level
			tree.append(node)
			tree = tree+(get_tree(queryset,node['id'],level+1))
	return tree

def get_tree_2(list,pid=0,level=1):
	tree = []
	for node in list:
		if node[1] == pid :
			node.append(level)
			tree.append(node)
			tree = tree+(get_tree_2(list,node[0],level+1))
	return tree

def create_tree(queryset):
	a_list = []
	for item in queryset:
		tt = []
		tt.append(item['id'])
		tt.append(item['pid'])
		tt.append(item['name'])
		a_list.append(tt)

	b_list = get_tree_2(a_list)
	agency_list = []
	for i in b_list:
		tt = []
		tt.append(i[0])
		if i[3] > 1 :
			ss = '|'+(i[3]-1)*'----'+i[2]
		else:
			ss = i[2]
		tt.append(ss)
		agency_list.append(tt)
	return agency_list

def isset(v):
	try:
		type(eval(v))
	except:
		return False
	else:
		return True