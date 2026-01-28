import openai
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HairImageSerializer
import os
import base64
import mimetypes

openai.api_key = os.getenv("OPENAI_API_KEY")

class HairChatbotView(APIView):
    def post(self, request):
        serializer = HairImageSerializer(data=request.data)
        if serializer.is_valid():
            image_obj = serializer.save()

            # Read the image file and encode it to base64
            with open(image_obj.image.path, 'rb') as image_file:
                base64_image = base64.b64encode(image_file.read()).decode('utf-8')
            
            # Get the MIME type of the image
            mime_type, _ = mimetypes.guess_type(image_obj.image.path)
            if not mime_type:
                mime_type = 'image/png'  # Default to PNG if unable to determine
            
            # Create data URL with base64 encoded image
            data_url = f"data:{mime_type};base64,{base64_image}"

            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "Analyze this hair image and give hair care advice in bengla."},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": data_url
                                }
                            }
                        ]
                    }
                ]
            )

            ai_reply = response.choices[0].message.content
            return Response({
                "message": ai_reply
            })

        return Response(serializer.errors, status=400)
