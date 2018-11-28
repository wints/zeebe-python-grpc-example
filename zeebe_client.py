import grpc
import gateway_pb2
import gateway_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:26500') as channel:
        stub = gateway_pb2_grpc.GatewayStub(channel)

        topologyResponse = stub.Topology(gateway_pb2.TopologyRequest())
        print(topologyResponse)

        listResponse = stub.ListWorkflows(gateway_pb2.ListWorkflowsRequest())
        print(listResponse)

        createResponse = stub.CreateWorkflowInstance(gateway_pb2.CreateWorkflowInstanceRequest(bpmnProcessId = 'simple-process', version = -1, payload = '{"orderId" : "ab1234"}'))
        print(createResponse)

        for jobResponse in stub.ActivateJobs(gateway_pb2.ActivateJobsRequest(type = 'payment-service', worker = 'zeebe-client-test', timeout = 1000, amount = 32)):
            for job in jobResponse.jobs:
                print(job)
                stub.CompleteJob(gateway_pb2.CompleteJobRequest(jobKey = job.key))

        stub.PublishMessage(gateway_pb2.PublishMessageRequest(name ='payment-confirmed', correlationKey = "ab1234", timeToLive = 100000, payload = '{"total-charged" : 25.95}' ))


if __name__ == '__main__':
    run()
