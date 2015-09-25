import plates
import repository
import os
if __name__ == '__main__':
    #plate = plates.get_plate('maya')
    #print "Plate:", plate
    #print list(plate.list_languages())
    repository.index_repository()
    template = repository.REPOSITORY['burnhill.maya.api.noisedeformer']
    template.set_project_name("noiseDeformer")
    template.set_destination("/home/fredrik.brannbacka/ClionProjects/noiseDeformer")
    template.write()