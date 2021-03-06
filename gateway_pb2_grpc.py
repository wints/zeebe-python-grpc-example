# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import gateway_pb2 as gateway__pb2


class GatewayStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Topology = channel.unary_unary(
        '/gateway_protocol.Gateway/Topology',
        request_serializer=gateway__pb2.TopologyRequest.SerializeToString,
        response_deserializer=gateway__pb2.TopologyResponse.FromString,
        )
    self.DeployWorkflow = channel.unary_unary(
        '/gateway_protocol.Gateway/DeployWorkflow',
        request_serializer=gateway__pb2.DeployWorkflowRequest.SerializeToString,
        response_deserializer=gateway__pb2.DeployWorkflowResponse.FromString,
        )
    self.PublishMessage = channel.unary_unary(
        '/gateway_protocol.Gateway/PublishMessage',
        request_serializer=gateway__pb2.PublishMessageRequest.SerializeToString,
        response_deserializer=gateway__pb2.PublishMessageResponse.FromString,
        )
    self.CreateJob = channel.unary_unary(
        '/gateway_protocol.Gateway/CreateJob',
        request_serializer=gateway__pb2.CreateJobRequest.SerializeToString,
        response_deserializer=gateway__pb2.CreateJobResponse.FromString,
        )
    self.UpdateJobRetries = channel.unary_unary(
        '/gateway_protocol.Gateway/UpdateJobRetries',
        request_serializer=gateway__pb2.UpdateJobRetriesRequest.SerializeToString,
        response_deserializer=gateway__pb2.UpdateJobRetriesResponse.FromString,
        )
    self.FailJob = channel.unary_unary(
        '/gateway_protocol.Gateway/FailJob',
        request_serializer=gateway__pb2.FailJobRequest.SerializeToString,
        response_deserializer=gateway__pb2.FailJobResponse.FromString,
        )
    self.CompleteJob = channel.unary_unary(
        '/gateway_protocol.Gateway/CompleteJob',
        request_serializer=gateway__pb2.CompleteJobRequest.SerializeToString,
        response_deserializer=gateway__pb2.CompleteJobResponse.FromString,
        )
    self.CreateWorkflowInstance = channel.unary_unary(
        '/gateway_protocol.Gateway/CreateWorkflowInstance',
        request_serializer=gateway__pb2.CreateWorkflowInstanceRequest.SerializeToString,
        response_deserializer=gateway__pb2.CreateWorkflowInstanceResponse.FromString,
        )
    self.CancelWorkflowInstance = channel.unary_unary(
        '/gateway_protocol.Gateway/CancelWorkflowInstance',
        request_serializer=gateway__pb2.CancelWorkflowInstanceRequest.SerializeToString,
        response_deserializer=gateway__pb2.CancelWorkflowInstanceResponse.FromString,
        )
    self.UpdateWorkflowInstancePayload = channel.unary_unary(
        '/gateway_protocol.Gateway/UpdateWorkflowInstancePayload',
        request_serializer=gateway__pb2.UpdateWorkflowInstancePayloadRequest.SerializeToString,
        response_deserializer=gateway__pb2.UpdateWorkflowInstancePayloadResponse.FromString,
        )
    self.ActivateJobs = channel.unary_stream(
        '/gateway_protocol.Gateway/ActivateJobs',
        request_serializer=gateway__pb2.ActivateJobsRequest.SerializeToString,
        response_deserializer=gateway__pb2.ActivateJobsResponse.FromString,
        )
    self.ListWorkflows = channel.unary_unary(
        '/gateway_protocol.Gateway/ListWorkflows',
        request_serializer=gateway__pb2.ListWorkflowsRequest.SerializeToString,
        response_deserializer=gateway__pb2.ListWorkflowsResponse.FromString,
        )
    self.GetWorkflow = channel.unary_unary(
        '/gateway_protocol.Gateway/GetWorkflow',
        request_serializer=gateway__pb2.GetWorkflowRequest.SerializeToString,
        response_deserializer=gateway__pb2.GetWorkflowResponse.FromString,
        )


class GatewayServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Topology(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeployWorkflow(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PublishMessage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateJob(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateJobRetries(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FailJob(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CompleteJob(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateWorkflowInstance(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CancelWorkflowInstance(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateWorkflowInstancePayload(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ActivateJobs(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListWorkflows(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetWorkflow(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GatewayServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Topology': grpc.unary_unary_rpc_method_handler(
          servicer.Topology,
          request_deserializer=gateway__pb2.TopologyRequest.FromString,
          response_serializer=gateway__pb2.TopologyResponse.SerializeToString,
      ),
      'DeployWorkflow': grpc.unary_unary_rpc_method_handler(
          servicer.DeployWorkflow,
          request_deserializer=gateway__pb2.DeployWorkflowRequest.FromString,
          response_serializer=gateway__pb2.DeployWorkflowResponse.SerializeToString,
      ),
      'PublishMessage': grpc.unary_unary_rpc_method_handler(
          servicer.PublishMessage,
          request_deserializer=gateway__pb2.PublishMessageRequest.FromString,
          response_serializer=gateway__pb2.PublishMessageResponse.SerializeToString,
      ),
      'CreateJob': grpc.unary_unary_rpc_method_handler(
          servicer.CreateJob,
          request_deserializer=gateway__pb2.CreateJobRequest.FromString,
          response_serializer=gateway__pb2.CreateJobResponse.SerializeToString,
      ),
      'UpdateJobRetries': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateJobRetries,
          request_deserializer=gateway__pb2.UpdateJobRetriesRequest.FromString,
          response_serializer=gateway__pb2.UpdateJobRetriesResponse.SerializeToString,
      ),
      'FailJob': grpc.unary_unary_rpc_method_handler(
          servicer.FailJob,
          request_deserializer=gateway__pb2.FailJobRequest.FromString,
          response_serializer=gateway__pb2.FailJobResponse.SerializeToString,
      ),
      'CompleteJob': grpc.unary_unary_rpc_method_handler(
          servicer.CompleteJob,
          request_deserializer=gateway__pb2.CompleteJobRequest.FromString,
          response_serializer=gateway__pb2.CompleteJobResponse.SerializeToString,
      ),
      'CreateWorkflowInstance': grpc.unary_unary_rpc_method_handler(
          servicer.CreateWorkflowInstance,
          request_deserializer=gateway__pb2.CreateWorkflowInstanceRequest.FromString,
          response_serializer=gateway__pb2.CreateWorkflowInstanceResponse.SerializeToString,
      ),
      'CancelWorkflowInstance': grpc.unary_unary_rpc_method_handler(
          servicer.CancelWorkflowInstance,
          request_deserializer=gateway__pb2.CancelWorkflowInstanceRequest.FromString,
          response_serializer=gateway__pb2.CancelWorkflowInstanceResponse.SerializeToString,
      ),
      'UpdateWorkflowInstancePayload': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateWorkflowInstancePayload,
          request_deserializer=gateway__pb2.UpdateWorkflowInstancePayloadRequest.FromString,
          response_serializer=gateway__pb2.UpdateWorkflowInstancePayloadResponse.SerializeToString,
      ),
      'ActivateJobs': grpc.unary_stream_rpc_method_handler(
          servicer.ActivateJobs,
          request_deserializer=gateway__pb2.ActivateJobsRequest.FromString,
          response_serializer=gateway__pb2.ActivateJobsResponse.SerializeToString,
      ),
      'ListWorkflows': grpc.unary_unary_rpc_method_handler(
          servicer.ListWorkflows,
          request_deserializer=gateway__pb2.ListWorkflowsRequest.FromString,
          response_serializer=gateway__pb2.ListWorkflowsResponse.SerializeToString,
      ),
      'GetWorkflow': grpc.unary_unary_rpc_method_handler(
          servicer.GetWorkflow,
          request_deserializer=gateway__pb2.GetWorkflowRequest.FromString,
          response_serializer=gateway__pb2.GetWorkflowResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'gateway_protocol.Gateway', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
