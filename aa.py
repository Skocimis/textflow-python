import src.textflowsms as tf

tf.useKey("UnndUImcIDysu03nSW1uSQvKxzoOaPbmSiqaKHczEvA51D6Dw3Rx0x5G5DjzyUJ6")

result = tf.sendVerificationSMS("+381690156360")
print(result.data.verification_code)
coderesult = tf.verifyCode("+381690156360", result.data.verification_code)
print(coderesult.valid)