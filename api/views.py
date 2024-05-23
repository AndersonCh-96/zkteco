from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.http.response import HttpResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from zk import ZK
from zk.exception import ZKError, ZKErrorConnection, ZKNetworkError
from .serializer import (
    UserCreateSerializer,
    UserGetSerializer,
    AttendanceSerializer,
    UserUpdateSerializer,
)

# Create conexion whit library Zk
conn = None
zk = ZK("192.168.0.122", port=4370)
datos_post = None


# Create your views here.
@csrf_exempt
@api_view(["GET", "POST", "DELETE", "PUT"])
def users(request, uid=None):

    # Conexion con dispositivo
    try:
        global conn, zk
        conn = zk.connect()
        conn.disable_device()
        users = conn.get_users()
        print("---Current total users----", len(users))
    except Exception as ex:
        return JsonResponse(ex)
    # ---------------------GET------------------------------#
    if request.method == "GET":
        try:
            serializer = UserGetSerializer(users, many=True)
            return JsonResponse({"success": True, "Users": serializer.data}, safe=False)
        except Exception as ex:
            return JsonResponse({"success": False, "error": str(ex)})

    # ----------------POST-------------------------------
    elif request.method == "POST":
        data = request.data
        serializer = UserCreateSerializer(data=data)
        if serializer.is_valid():
            userData = serializer.validated_data
            try:
                conn.set_user(
                    name=userData.get("name"),
                    privilege=userData.get("privilege"),
                    password=userData.get("password"),
                )
                conn.get_users()
                return JsonResponse({"success": True, "Data": userData})
            except Exception as ex:
                print("Errores", ex)
                return JsonResponse({"success": False, "error": str(ex)})
        return JsonResponse({"success": False, "errors": serializer.errors})
    # ------------------------UPDATE USER -------------------------------------
    elif request.method == "PUT":

        data = request.data
        serializer = UserUpdateSerializer(data=data)
        if serializer.is_valid():
            userData = serializer.validated_data
            try:
                conn.set_user(
                    uid=userData.get("uid"),
                    name=userData.get("name"),
                    privilege=userData.get("privilege"),
                    password=userData.get("password"),
                )
                conn.get_users()
                return JsonResponse({"success": True, "Data": userData})
            except Exception as ex:
                print("Errores", ex)
                return JsonResponse({"success": False, "error": str(ex)})
        return JsonResponse({"success": False, "errors": serializer.errors})

    # --------------------DELETE-----------------------------------------------
    elif request.method == "DELETE":
        try:
            data = int(uid)
            conn = zk.connect()
            conn.delete_user(data)
            return JsonResponse({"success": True, "data": data})
        except Exception as ex:
            return JsonResponse({"success": False, "Error": str(ex)})


@csrf_exempt
def attendance_list(request):
    try:
        global conn, zk
        conn = zk.connect()
        print("Disabling device ...")
        conn.disable_device()
        print("--- Get attendances ---")
        att_list = conn.get_attendance()
        att_list = AttendanceSerializer(att_list, many=True)
        print("Lista de datos: ", att_list)

    except Exception as ex:
        print("Process terminate : {}".format(ex))
        return JsonResponse(ex)

    if request.method == "GET":
        return JsonResponse(att_list.data, safe=False)


@csrf_exempt
def attendance_live_capture(request):

    # Start monitoring and transmiting real-time data

    # if not zk.connect():
    #     raise ZKErrorConnection("Conexión no establecida")
    # try:
    #     conn = zk.connect()
    #     for attendance in conn.live_capture():
    #         if attendance is None:
    #             pass
    #         else:
    #             print("Sinserializar: ", attendance)
    #             print("#############################")
    #             att_data = AttendanceSerializer(attendance, many=True)
    #             print("Attendance real time", att_data.data)
    #             att_all_list = conn.get_attendance()
    #             print("Atendance list", att_all_list)
    #             JsonResponse(att_data, safe=False)
    #             # payload = {"current_att_data": att_all_list, "att_all_list": att_data}
    #             # res = requests.post(
    #             #     "http://localhost/hrm/api/zkteco/att-new-record", params=payload)
    #             # print(res.json())
    # except UnboundLocalError:
    #     print(" I am unable to connect to the server")
    # except Exception as e:
    #     print("Process terminate : {}".format(e))
    # finally:
    pass


@csrf_exempt
@api_view(["POST"])
def refresh(request):
    try:

        global conn, zk
        # Establecer una conexión con el dispositivo ZKTeco
        conn = zk.connect()
        # Limpiar las entradas
        conn.clear_attendance()

        # Devolver una respuesta de éxito
        return HttpResponse(
            {"mensaje": "El dispositivo ha sido apagado correctamente"}, status=200
        )

    except Exception as e:
        # Si ocurre algún error, devolver una respuesta de error
        return HttpResponse({"error": str(e)}, status=500)

    if request.method == "GET":
        return JsonResponse(att_list.data, safe=False)


@csrf_exempt
@api_view(["GET", "POST"])
def testeo(request):
    try:
        if request.method == "POST":
            data = request.data
            attendances = AttendanceSerializer(data, many=True)
            datos_post = attendances
            print("datos entrando", datos_post)
            return HttpResponse({"message": "Ok"})
    except:
        print("An exception occurred")
