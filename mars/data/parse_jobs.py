from flask_restful import reqparse

parser_ = reqparse.RequestParser()
parser_.add_argument('team_leader', required=True)
parser_.add_argument('job', required=True)
parser_.add_argument('work_size', required=True, type=int)
parser_.add_argument('collaborators', required=True)
parser_.add_argument('is_finished', required=True, type=bool)
