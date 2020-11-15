
import maya.cmds as cmds
import os.path as path

#MODIFY THE PATH
root_dir = 'D:/Masterclass/NCCA2019_ChefEnvironment'
texture_path=root_dir+'/sourceimages'

def createMaterial(obj_name, texture_node):
    shader = cmds.shadingNode('PxrSurface', asShader=True, name="MAT_"+obj_name)
    diffuse_texture = cmds.shadingNode(texture_node, asTexture=True, name='TEX_'+obj_name+'_Diffuse')
    spec_texture = cmds.shadingNode(texture_node, asTexture=True, name='TEX_'+obj_name+'_Spec')
    gloss_texture = cmds.shadingNode(texture_node, asTexture=True, name='TEX_'+obj_name+'_Gloss')
    cmds.connectAttr(diffuse_texture+'.resultRGB', shader+'.diffuseColor')
    cmds.connectAttr(spec_texture+'.resultRGB', shader+'.specularFaceColor')
    cmds.connectAttr(gloss_texture+'.resultRGB', shader+'.roughSpecularFaceColor')
    
    return shader

def assignTexture (obj_name, channel, filepath):
    node_name = 'TEX_'+obj_name+channel
    ext = '.ptx'
    filepath += '/%s_textures'%obj_name + '/%s%s'%(obj_name, channel) + ext
    if path.exists(filepath):
        if cmds.objExists(node_name):
            cmds.setAttr(node_name+'.filename', filepath,type='string')
            cmds.setAttr(node_name+'.filter', 6)
            cmds.setAttr(node_name+'.linearize', 1)
            return filepath
        else: print("No such node exists")
    else: print("No such file exists: %s"%filepath)
    

obj_name='Rag'
createMaterial(obj_name, 'PxrPtexture')
assignTexture(obj_name, '_Diffuse', texture_path)
assignTexture(obj_name, '_Spec', texture_path)
assignTexture(obj_name, '_Gloss', texture_path)


