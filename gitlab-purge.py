import requests
from sys import argv

endpoint = 'https://gitlab.com/api/v4/'
auth  = argv[1]
purgeRepo = 101
response = requests.get(endpoint + 'projects/',params="per_page=100",
                        headers={
                               "PRIVATE-TOKEN": auth
                        }
                        )


for data in response.json():
    project_id = data["id"]
    if project_id != purgeRepo:
        print("Delete pipeline for " +  data["name"])
        while (  requests.get(endpoint + 'projects/' + str(project_id) + '/pipelines/',  headers={"PRIVATE-TOKEN": auth}).json() ):
            pipelines_data = requests.get(endpoint + 'projects/' + str(project_id) + '/pipelines/',  headers={"PRIVATE-TOKEN": auth}).json()
            for i in pipelines_data:
                pipeline_id = i["id"]
                todelete = requests.delete(endpoint + 'projects/' + str(project_id) + '/pipelines/' + str(pipeline_id),  headers={"PRIVATE-TOKEN": auth})
                if todelete:
                    print("Pipeline " + str(pipeline_id) + " deleted")
                else:
                    print("Pipeline" + str(pipeline_id) + " failed to delete")



