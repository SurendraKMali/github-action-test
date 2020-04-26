from urllib.request import Request, urlopen, URLError, HTTPError
import json

def slack_notif(notif): #, channel_name, user_name):
    """ 
    :param notif: Massage to send on Slack Channel 
    :return: None 
    """

    hook_url = "https://hooks.slack.com/services/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"
    # Slack Message
    slack_message = {
        'channel': 'epi_poc',  # 'cypher_aws_alert',
        'text':  str(notif),
        'username': 'POC_Bot',
        'icon_emoji': ':robot_face:'
    }

    req = Request(hook_url, json.dumps(slack_message).encode('utf-8'))
    try:
        response = urlopen(req)
        response.read()

    except HTTPError as e:
        print("Request failed: %d %s", e.code, e.reason)
    except URLError as e:
        print("Server connection failed: %s", e.reason)

if __name__=="__main__":

    slack_notif("DataWareHouse_Deploy triggered")