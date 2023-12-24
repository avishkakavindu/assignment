from rest_framework.views import APIView
from elasticsearch import Elasticsearch
from django.http import JsonResponse

es = Elasticsearch([{'host': '127.0.0.1', 'port': 9200, 'scheme': 'http'}], http_auth=('elastic', '[password]'))  # Update with your Elasticsearch host and port

class AddToElasticsearch(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            es.index(index='application_status', body=data)
            return JsonResponse({'message': 'Data added to Elasticsearch successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

class GetApplicationStatus(APIView):
    def get(self, request, *args, **kwargs):
        try:
            res = es.search(index='application_status', size=1, sort='@timestamp:desc', _source=['service_name', 'service_status', 'host_name'])
            if res['hits']['total']['value'] > 0:
                return JsonResponse(res['hits']['hits'][0]['_source'])
            else:
                return JsonResponse({'message': 'No application status found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

class GetServiceStatus(APIView):
    def get(self, request, service_name, *args, **kwargs):
        try:
            res = es.search(index='application_status', body={'query': {'match': {'service_name': service_name}}}, size=1, sort='@timestamp:desc', _source=['service_name', 'service_status', 'host_name'])
            if res['hits']['total']['value'] > 0:
                return JsonResponse(res['hits']['hits'][0]['_source'])
            else:
                return JsonResponse({'message': f'No status found for {service_name}'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
