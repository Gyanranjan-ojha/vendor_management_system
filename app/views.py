from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .auth.authentication import APITokenAuthentication
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer

class VendorListCreateAPIView(APIView):

    authentication_classes = [APITokenAuthentication]
    permission_classes = [AllowAny]

    def get(self, request):
        try:
            vendors = Vendor.objects.values('id', 'name', 'contact_details', 'address', 'vendor_code')
            serializer = VendorSerializer(vendors, many=True)
            if serializer.data:
                return Response({"message": "All Vendors Data", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Vendors data not available"}, status=status.HTTP_204_NO_CONTENT)
        except Exception:
            return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = VendorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Sucessfully vendor created", "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class VendorRetrieveUpdateDestroyAPIView(APIView):

    authentication_classes = [APITokenAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, pk):
        try:
            vendor = Vendor.objects.values('id', 'name', 'contact_details', 'address', 'vendor_code').get(pk=pk)
            serializer = VendorSerializer(vendor)
            return Response({"message": "Vendor Data", "data": serializer.data}, status=status.HTTP_200_OK)
        except Vendor.DoesNotExist:
            return Response({"error": "Vendor does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            if 'id' in request.data.keys():
                return Response({"error": "Can't be update the id of the vendor,remove the id."}, status=status.HTTP_400_BAD_REQUEST)
            
            vendor = Vendor.objects.get(pk=pk)
            serializer = VendorSerializer(vendor, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Sucessfully updated", "data": serializer.data}, status=status.HTTP_200_OK)
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            
        except Vendor.DoesNotExist:
            return Response({"error": "Vendor does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def delete(self, request, pk):
        try:
            vendor = Vendor.objects.get(pk=pk)
            vendor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Vendor.DoesNotExist:
            return Response({"error": "Vendor does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PurchaseOrderListCreateAPIView(APIView):

    authentication_classes = [APITokenAuthentication]
    permission_classes = [AllowAny]

    def get(self, request):
        try:
            purchase_orders = PurchaseOrder.objects.select_related('vendor_id')
            serializer = PurchaseOrderSerializer(purchase_orders, many=True)
            if serializer.data:
                return Response({"message": "All Purchase orders Data", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Purchase orders data not available"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = PurchaseOrderSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Sucessfully purchase order created", "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PurchaseOrderRetrieveUpdateDestroyAPIView(APIView):

    authentication_classes = [APITokenAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, pk):
        try:
            purchase_order = PurchaseOrder.objects.values('id', 'po_number', 'order_date', 'status').get(pk=pk)
            serializer = PurchaseOrderSerializer(purchase_order)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PurchaseOrder.DoesNotExist:
            return Response({"error": "Purchase order does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(f"Error in GET request of PurchaseOrderRetrieveUpdateDestroyAPIView: {e}")
            return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            purchase_order = PurchaseOrder.objects.get(pk=pk)
            serializer = PurchaseOrderSerializer(purchase_order, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except PurchaseOrder.DoesNotExist:
            return Response({"error": "Purchase order does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(f"Error in PUT request of PurchaseOrderRetrieveUpdateDestroyAPIView: {e}")
            return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            purchase_order = PurchaseOrder.objects.get(pk=pk)
            purchase_order.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except PurchaseOrder.DoesNotExist:
            return Response({"error": "Purchase order does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(f"Error in DELETE request of PurchaseOrderRetrieveUpdateDestroyAPIView: {e}")
            return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)