system_theme_color = '#303030'
source_label_color = '#00C957'
target_label_color = '#EE2C2C'


def prolog(sourceCubeName, targetCubeName, sourceCount, targetCount, dimSourceNames, dimTargetNames,
           selected_items_source, selected_items_target):
    if sourceCubeName != 'Select Source Cube' and targetCubeName == 'Select Target Cube':
        cubeName = sourceCubeName
    else:
        cubeName = targetCubeName
    p0 = f'''CubeName = '{cubeName}';
CubeSetLogChanges (CubeName, 0);'''

    p1 = f'''
#******* Source Cube ***********************************

vProcessName = GetProcessName;

v_CubeSourceName = '{sourceCubeName}';
v_ViewSourceName = 'Source'|'_'|v_CubeSourceName|'_'|vProcessName;'''
    p4 = '''
IF(VIEWEXISTS(v_CubeSourceName, v_ViewSourceName)=1);
VIEWDESTROY(v_CubeSourceName, v_ViewSourceName);
ENDIF;'''
    p6 = '''
VIEWCREATE(v_CubeSourceName, v_ViewSourceName);

ViewExtractSkipCalcsSet(v_CubeSourceName, v_ViewSourceName, 1);
ViewExtractSkipRuleValuesSet(v_CubeSourceName, v_ViewSourceName, 0);
ViewExtractSkipZeroesSet(v_CubeSourceName, v_ViewSourceName, 1);'''
    p9 = '''
#Data source assignment
DataSourceType = 'View';
DataSourceNameForServer = v_CubeSourceName;
DatasourceCubeview = v_ViewSourceName;'''
    tempPrologSource = ''
    tempP3source = ''

    for j in range(int(sourceCount) - 1, -1, -1):
        p2 = '''
v_DimSourceName{} = '{}';'''.format(j + 1, dimSourceNames[j])
        tempPrologSource = p2 + tempPrologSource
    for j in range(int(sourceCount) - 1, -1, -1):
        p3 = '''
v_SubSourceName{} = v_DimSourceName{}|'_'|v_ViewSourceName;'''.format(j + 1, j + 1)
        tempP3source = p3 + tempP3source

    tempSource = ""
    tempMdx = ""
    tempAssign = ""

    for j in range(int(sourceCount) - 1, -1, -1):
        p5 = f'''
IF(SUBSETEXISTS(v_DimSourceName{j + 1}, v_SubSourceName{j + 1})=1);
SUBSETDESTROY(v_DimSourceName{j + 1}, v_SubSourceName{j + 1}); 
ENDIF;'''
        tempSource = p5 + tempSource
    for j in range(int(sourceCount) - 1, -1, -1):
        if not selected_items_source:
            if dimSourceNames[j] == 'Scenario':
                p7 = f'''
SubsetCreate(v_DimSourceName{j + 1}, v_SubSourceName{j + 1}, 0);
SubsetElementInsert(v_DimSourceName{j + 1}, v_SubSourceName{j + 1}, p_Scenario, 1);\n'''
            elif dimSourceNames[j] == 'Version' or dimSourceNames[j] == '5_Versiyon':
                p7 = f'''
SubsetCreate(v_DimSourceName{j + 1}, v_SubSourceName{j + 1}, 0);
SubsetElementInsert(v_DimSourceName{j + 1}, v_SubSourceName{j + 1}, p_Version, 1);\n'''
            else:
                p7 = f'''
MDX{j + 1} = '{{TM1FILTERBYLEVEL({{TM1SUBSETALL(['|v_DimSourceName{j + 1}|'])}},0)}}';
SUBSETCREATEBYMDX(v_SubSourceName{j + 1}, MDX{j + 1}, 0);\n'''
            tempMdx = p7 + tempMdx
        elif list(set(map(int, [item[0] for item in selected_items_source]))).__contains__(j):
            p7_subCreate = f'''
SubsetCreate(v_DimSourceName{j + 1}, v_SubSourceName{j + 1}, 0);'''
            for z in range(len(selected_items_source) - 1, -1, -1):
                if j == list(map(int, [item[0] for item in selected_items_source]))[z]:
                    p7_sub_Element = f'''
SubsetElementInsert(v_DimSourceName{j + 1}, v_SubSourceName{j + 1}, '{selected_items_source[z][1:]}', 1);'''
                    tempMdx = p7_sub_Element + tempMdx
            tempMdx = p7_subCreate + tempMdx
        else:
            p7 = f'''
MDX{j + 1} = '{{TM1FILTERBYLEVEL({{TM1SUBSETALL(['|v_DimSourceName{j + 1}|'])}},0)}}';
SUBSETCREATEBYMDX(v_SubSourceName{j + 1}, MDX{j + 1}, 0);\n'''
            tempMdx = p7 + tempMdx

    for j in range(int(sourceCount) - 1, -1, -1):
        p8 = f'''
VIEWSUBSETASSIGN(v_CubeSourceName, v_ViewSourceName, v_DimSourceName{j + 1}, v_SubSourceName{j + 1});'''
        tempAssign = p8 + tempAssign

    # TARGET CUBE
    p1_t = f'''
#******* Target Cube ***********************************

v_CubeName = '{targetCubeName}';
v_ViewName = 'VZO'|'_'|v_CubeName|'_'|vProcessName;'''
    p1_t_v2 = f'''
#******* Target Cube ***********************************

vProcessName = GetProcessName;

v_CubeName = '{targetCubeName}';
v_ViewName = 'VZO'|'_'|v_CubeName|'_'|vProcessName;'''
    p4_t = '''
IF(VIEWEXISTS(v_CubeName, v_ViewName)=1);
VIEWDESTROY(v_CubeName, v_ViewName);
ENDIF;'''
    p6_t = '''
VIEWCREATE(v_CubeName, v_ViewName);'''
    p9_t = '''
ViewZeroOut(v_CubeName, v_ViewName);'''
    tempPrologSource_t = ''
    tempP3source_t = ''
    tempSource_t = ''
    tempMdx_t = ''
    tempAssign_t = ''
    for j in range(targetCount - 1, -1, -1):
        p2_t = '''
v_Dim{}Name = '{}';'''.format(j + 1, dimTargetNames[j])
        tempPrologSource_t = p2_t + str(tempPrologSource_t)
    for j in range(targetCount - 1, -1, -1):
        p3_t = '''
v_Subs{}Name = v_Dim{}Name|'_'|v_ViewName;'''.format(j + 1, j + 1)
        tempP3source_t = p3_t + str(tempP3source_t)
    for j in range(targetCount - 1, -1, -1):
        p5_t = '''
IF(SUBSETEXISTS(v_Dim{}Name, v_Subs{}Name)=1);
SUBSETDESTROY(v_Dim{}Name, v_Subs{}Name);
ENDIF;'''.format(j + 1, j + 1, j + 1, j + 1)
        tempSource_t = p5_t + str(tempSource_t)

    for j in range(targetCount - 1, -1, -1):
        if sourceCubeName == targetCubeName:
            if str(dimTargetNames[j]) == 'Scenario':
                p7_t = f'''
SubsetCreate(v_Dim{j + 1}Name, v_Subs{j + 1}Name, 0);
SubsetElementInsert(v_Dim{j + 1}Name, v_Subs{j + 1}Name, p_TScenario, 1);\n'''
                tempMdx_t = p7_t + str(tempMdx_t)
            elif str(dimTargetNames[j]) == 'Version':
                p7_t = f'''
SubsetCreate(v_Dim{j + 1}Name, v_Subs{j + 1}Name, 0);
SubsetElementInsert(v_Dim{j + 1}Name, v_Subs{j + 1}Name, p_TVersion, 1);\n'''
                tempMdx_t = p7_t + str(tempMdx_t)
            else:
                if not selected_items_target:
                    if str(dimTargetNames[j]) == 'Scenario':
                        p7_t = '''
SubsetCreate(v_Dim{}Name, v_Subs{}Name, 0);
SubsetElementInsert(v_Dim{}Name, v_Subs{}Name, p_Scenario, 1);\n'''.format(j + 1, j + 1, j + 1, j + 1)
                        tempMdx_t = p7_t + str(tempMdx_t)
                    elif str(dimTargetNames[j]) == 'Version' or str(dimTargetNames[j]) == '5_Versiyon':
                        p7_t = '''
SubsetCreate(v_Dim{}Name, v_Subs{}Name, 0);
SubsetElementInsert(v_Dim{}Name, v_Subs{}Name, p_Version, 1);\n'''.format(j + 1, j + 1, j + 1, j + 1)
                        tempMdx_t = p7_t + str(tempMdx_t)
                    else:
                        p7_t = f'''
MDX{j + 1} = '{{TM1FILTERBYLEVEL({{TM1SUBSETALL(['|v_Dim{j + 1}Name|'])}},0)}}';
SUBSETCREATEBYMDX(v_Subs{j + 1}Name, MDX{j + 1}, 0);\n'''
                        tempMdx_t = p7_t + tempMdx_t
                elif list(set(map(int, [item[0] for item in selected_items_target]))).__contains__(j):
                    p7_t_subCreate = f'''
SubsetCreate(v_Dim{j + 1}Name, v_Subs{j + 1}Name, 0);'''
                    for z in range((len(selected_items_target)) - 1, -1, -1):
                        if j == list(map(int, [item[0] for item in selected_items_target]))[z]:
                            p7_t_sub_Element = f'''
SubsetElementInsert(v_Dim{j + 1}Name, v_Subs{j + 1}Name, '{selected_items_target[z][1:]}', 1);'''
                            tempMdx_t = p7_t_sub_Element + tempMdx_t
                    tempMdx_t = p7_t_subCreate + tempMdx_t
                else:
                    p7_t = f'''
MDX{j + 1} = '{{TM1FILTERBYLEVEL({{TM1SUBSETALL(['|v_Dim{j + 1}Name|'])}},0)}}';
SUBSETCREATEBYMDX(v_Subs{j + 1}Name, MDX{j + 1}, 0);\n'''
                    tempMdx_t = p7_t + tempMdx_t
        else:
            if not selected_items_target:
                if str(dimTargetNames[j]) == 'Scenario':
                    p7_t = '''
SubsetCreate(v_Dim{}Name, v_Subs{}Name, 0);
SubsetElementInsert(v_Dim{}Name, v_Subs{}Name, p_Scenario, 1);\n'''.format(j + 1, j + 1, j + 1, j + 1)
                    tempMdx_t = p7_t + str(tempMdx_t)
                elif str(dimTargetNames[j]) == 'Version' or str(dimTargetNames[j]) == '5_Versiyon':
                    p7_t = '''
SubsetCreate(v_Dim{}Name, v_Subs{}Name, 0);
SubsetElementInsert(v_Dim{}Name, v_Subs{}Name, p_Version, 1);\n'''.format(j + 1, j + 1, j + 1, j + 1)
                    tempMdx_t = p7_t + str(tempMdx_t)
                else:
                    p7_t = f'''
MDX{j + 1} = '{{TM1FILTERBYLEVEL({{TM1SUBSETALL(['|v_Dim{j + 1}Name|'])}},0)}}';
SUBSETCREATEBYMDX(v_Subs{j + 1}Name, MDX{j + 1}, 0);\n'''
                    tempMdx_t = p7_t + tempMdx_t
            elif list(set(map(int, [item[0] for item in selected_items_target]))).__contains__(j):
                p7_t_subCreate = f'''
SubsetCreate(v_Dim{j + 1}Name, v_Subs{j + 1}Name, 0);'''
                for z in range((len(selected_items_target)) - 1, -1, -1):
                    if j == list(map(int, [item[0] for item in selected_items_target]))[z]:
                        p7_t_sub_Element = f'''
SubsetElementInsert(v_Dim{j + 1}Name, v_Subs{j + 1}Name, '{selected_items_target[z][1:]}', 1);'''
                        tempMdx_t = p7_t_sub_Element + tempMdx_t
                tempMdx_t = p7_t_subCreate + tempMdx_t
            else:
                p7_t = f'''
MDX{j + 1} = '{{TM1FILTERBYLEVEL({{TM1SUBSETALL(['|v_Dim{j + 1}Name|'])}},0)}}';
SUBSETCREATEBYMDX(v_Subs{j + 1}Name, MDX{j + 1}, 0);\n'''
                tempMdx_t = p7_t + tempMdx_t

    for j in range(targetCount - 1, -1, -1):
        p8_t = '''
VIEWSUBSETASSIGN(v_CubeName, v_ViewName, v_Dim{}Name, v_Subs{}Name);'''.format(j + 1, j + 1)
        tempAssign_t = p8_t + str(tempAssign_t)

    if sourceCubeName != 'Select Source Cube' and targetCubeName == 'Select Target Cube':
        return '{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}{}\n{}'.format(p0, p1, tempPrologSource, tempP3source, p4, tempSource, p6,
                                                             tempMdx, tempAssign, p9)
    elif sourceCubeName == 'Select Source Cube' and targetCubeName != 'Select Target Cube':
        return '{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}{}\n{}'.format(p0, p1_t_v2, tempPrologSource_t, tempP3source_t, p4_t,
                                                             tempSource_t, p6_t, tempMdx_t, tempAssign_t, p9_t)
    else:
        return '{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}{}\n{}'.format(p0, p1, tempPrologSource,
                                                                                               tempP3source, p4,
                                                                                               tempSource,
                                                                                               p6, tempMdx, tempAssign,
                                                                                               p9,
                                                                                               p1_t, tempPrologSource_t,
                                                                                               tempP3source_t, p4_t,
                                                                                               tempSource_t, p6_t,
                                                                                               tempMdx_t, tempAssign_t,
                                                                                               p9_t)


def epilog(sourceCubeName, targetCubeName, sourceCount, targetCount):
    if sourceCubeName != 'Select Source Cube' and targetCubeName == 'Select Target Cube':
        cubeName = sourceCubeName
    else:
        cubeName = targetCubeName
    e0 = f'''CubeName = '{cubeName}';
CubeSetLogChanges(CubeName, 1);'''
    e1 = '''
###---Source View Destroy----###

IF(VIEWEXISTS(v_CubeSourceName, v_ViewSourceName)=1);
VIEWDESTROY(v_CubeSourceName,v_ViewSourceName);
ENDIF;'''
    e2 = '''###---Target View Destroy----###

IF(VIEWEXISTS(v_CubeName, v_ViewName)=1);
VIEWDESTROY(v_CubeName,v_ViewName);
ENDIF;'''

    temp_source = ''
    temp_vzo = ''

    for j in range(int(sourceCount), 0, -1):
        e2_source = f'''IF(SUBSETEXISTS(v_DimSourceName{j},v_SubSourceName{j})=1);
SUBSETDESTROY(v_DimSourceName{j},v_SubSourceName{j}); 
ENDIF;\n'''
        temp_source = e2_source + temp_source

    for j in range(targetCount, 0, -1):
        e2_vzo = f'''IF(SUBSETEXISTS(v_Dim{j}Name,v_Subs{j}Name)=1);
SUBSETDESTROY(v_Dim{j}Name,v_Subs{j}Name); 
ENDIF;\n'''
        temp_vzo = e2_vzo + temp_vzo

    if sourceCubeName != 'Select Source Cube' and targetCubeName == 'Select Target Cube':
        return '{}\n{}\n\n{}'.format(e0, e1, temp_source)
    elif sourceCubeName == 'Select Source Cube' and targetCubeName != 'Select Target Cube':
        return '{}\n\n{}\n\n{}'.format(e0, e2, temp_vzo)
    else:
        return '{}\n{}\n\n{}\n{}\n\n{}'.format(e0, e1, temp_source, e2, temp_vzo)
