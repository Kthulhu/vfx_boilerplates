import repository

if __name__ == '__main__':
    repository.index_repository()
    print repository.REPOSITORY

    template = repository.REPOSITORY['burnhill.maya.api.noisedeformer']
    template.set_project_name("noiseDeformer")
    template.set_destination("/tmp/test")
    template.write()

    template = repository.REPOSITORY['burnhill.arnold.shaders.constant']
    template.set_project_name("constantShader")
    template.set_destination("/tmp/testShader")
    template.write()