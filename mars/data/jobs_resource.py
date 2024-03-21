from flask_restful import reqparse, abort, Api, Resource
from werkzeug.security import generate_password_hash

from mars.data import db_session
from mars.data.jobs import Jobs
from mars.data.reg_parse_user import parser
from mars.data.parse_jobs import parser_
from flask import jsonify


def set_password(password):
    return generate_password_hash(password)


def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    user = session.query(Jobs).get(user_id)
    if not user:
        abort(404, message=f"Jobs {user_id} not found")


class JobsResource(Resource):
    def get(self, job_id):
        abort_if_user_not_found(job_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(job_id)
        return jsonify(
            {'jobs': {'jobs': jobs.id, 'team_leader': jobs.team_leader, 'job': jobs.job, 'work_size': jobs.work_size,
                      'collaborators': jobs.collaborators, 'is_finished': jobs.is_finished}})

    def delete(self, job_id):
        abort_if_user_not_found(job_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(job_id)
        session.delete(jobs)
        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify(
            {'jobs': [{'id': job_.id, 'team_leader': job_.team_leader, 'job': job_.job, 'work_size': job_.work_size,
                       'collaborators': job_.collaborators, 'is_finished': job_.is_finished} for job_ in jobs]})

    def post(self):
        args = parser_.parse_args()
        session = db_session.create_session()
        jobs = Jobs(
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            is_finished=args['is_finished'])
        session.add(jobs)
        session.commit()
        return jsonify({'id': jobs.id})
