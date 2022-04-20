from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from flask_login import login_user, logout_user, login_required, current_user
from .models import *
from . import db
import json
views = Blueprint("views", __name__)

@views.route("/home1")
@login_required
def data():
    # projects5 =  project5.query.all()
    # projects6 =  project6.query.all()
    # projects7 =  project7.query.all()
    # projects8 =  project8.query.all()
    return render_template("home2.html", user=current_user,)#projects5=projects5,projects6=projects6,projects7=projects7,projects8=projects8)



@views.route("/home/",methods=['GET', 'POST'])
@login_required
def home():
    import pdb
    pdb.set_trace()
    qry =  Project6.query.filter(Project6.id==id)
   # user = User.query.filter_by(username=username).first()  
    if request.method == 'POST':
       
       project = request.form.get("project")
       if not project:
           flash('project cannot be empty', category='error')
       resource_type = request.form.get("resource_type")
       if not resource_type:
           flash('resource_type cannot be empty', category='error')
      # email_exists = Project5.query.filter_by(project=project).first()
       if resource_type=='Compute instance':
          machine_type = request.form.get("machine_type")
          zone = request.form.get("zone")
          service_account = request.form.get("service_account")
          access_scopes = request.form.get("access_scopes")
          approver = request.form.get("approver")
          if not machine_type:
             flash('machine_type cannot be empty', category='error')
          if not zone:
             flash('zone cannot be empty', category='error')
          if not service_account:
             flash('service_account cannot be empty', category='error')
          if not access_scopes:
             flash('access_scopes cannot be empty', category='error')
          if not approver:
             flash('approver cannot be empty', category='error')
        
          project36 = Project6(project=project, resource_type=resource_type,machine_type=machine_type,zone=zone,service_account=service_account,access_scopes=access_scopes,approver=approver,author=current_user.id)
          db.session.add(project36)
          db.session.commit()
          login_user(project36, remember=True)
          flash('Successfully Save!', category='success')
          return redirect(url_for('views.rating1'))
          #return render_template("home.html", user=current_user)
         # return redirect(url_for('views.home'))

       elif resource_type=='Service account':
          resource_type = request.form.get("resource_type")
       elif resource_type=='Big query':
          dataset_name = request.form.get("dataset_name")
          data_location = request.form.get("data_location")
          approver = request.form.get("approver")
          if not dataset_name:
             flash('dataset_name cannot be empty', category='error')
          if not data_location:
             flash('data_location cannot be empty', category='error')
          if not approver:
             flash('approver cannot be empty', category='error')
        
          project37 = Project7(project=project, resource_type=resource_type,dataset_name=dataset_name,data_location=data_location,approver=approver,author=current_user.id)
          db.session.add(project37)
          db.session.commit()
          login_user(project37, remember=True)
          flash('Successfully Save!', category='success')
          return redirect(url_for('views.rating2'))
         # return render_template("home.html", user=current_user)
         # return redirect(url_for('views.home'))

       elif resource_type=='GCS bucket':
          Gcs_bucket_Location = request.form.get("Gcs_bucket_Location")
          storage_class = request.form.get("storage_class")
          role = request.form.get("role")
          service_account1 = request.form.get("service_account1")
          access_control = request.form.get("access_control")
          approver = request.form.get("approver")
          if not Gcs_bucket_Location:
           flash('Gcs_bucket_Location cannot be empty', category='error') 
          if not storage_class:
              flash('storage_class cannot be empty', category='error')
          if not role:
              flash('role cannot be empty', category='error')
          if not service_account1:
              flash('service_account1 cannot be empty', category='error')
          if not access_control:
              flash('access_control cannot be empty', category='error')            
          if not approver:
             flash('approver cannot be empty', category='error')
        
                   
          project38 = Project8(project=project, resource_type=resource_type,Gcs_bucket_Location=Gcs_bucket_Location,storage_class=storage_class,role=role,service_account1=service_account1,access_control=access_control,approver=approver,author=current_user.id)
          db.session.add(project38)
          db.session.commit()
          login_user(project38, remember=True)
          flash('Successfully Save!', category='success')
          #return render_template("home.html", user=current_user)
          return redirect(url_for('views.rating3'))

       approver = request.form.get("approver")
       if not approver:
           flash('approver cannot be empty', category='error')
    
       else: 
                   
            project35 = Project5(project=project, resource_type=resource_type,approver=approver,author=current_user.id)
            db.session.add(project35)
            db.session.commit()
            login_user(project35, remember=True)
            flash('Successfully Save!', category='success')
           # return render_template("home.html", user=current_user)
            return redirect(url_for('views.rating'))

    return render_template("home2.html", user=current_user)




@views.route('/rating')
def rating():
  import pdb
  #pdb.set_trace()
  
  movies = Project5.query.all()
  print(movies)
  results = [{
  'project':movie.project,
  'resource_type':movie.resource_type,
  
  'approver':movie.approver } for movie in movies]
  with open('Service account.json', 'w') as json_file:
       json.dump(results, json_file)
  return jsonify({
    'success':True,
    'results':results,
    'count':len(movies)
  })
  
  
@views.route('/rating1')
def rating1():
  import pdb
  #pdb.set_trace()
  
  movies = Project6.query.all()
  print(movies)
  results = [{
  'project':movie.project,
  'resource_type':movie.resource_type,
  'machine_type':movie.machine_type,
  'zone':movie.zone,
  'service_account':movie.service_account,
  'access_scopes':movie.access_scopes,
  
  'approver':movie.approver } for movie in movies]
  with open('Compute instance.json', 'w') as json_file:
       json.dump(results, json_file)
  return jsonify({
    'success':True,
    'results':results,
    'count':len(movies)
  })
  
@views.route('/rating2')
def rating2():
  import pdb
  #pdb.set_trace()
  
  movies = Project7.query.all()
  print(movies)
  results = [{
  'project':movie.project,
  'resource_type':movie.resource_type,
  
  'dataset_name':movie.dataset_name,
  'data_location':movie.data_location,
 
  'approver':movie.approver } for movie in movies]
  with open('Big query.json', 'w') as json_file:
       json.dump(results, json_file)
  return jsonify({
    'success':True,
    'results':results,
    'count':len(movies)
  })

@views.route('/rating3')
def rating3():
  import pdb
  #pdb.set_trace()
  
  movies = Project8.query.all()
  print(movies)
  results = [{
  'project':movie.project,
  'resource_type':movie.resource_type,
  
  'Gcs_bucket_Location':movie.Gcs_bucket_Location,
  'storage_class':movie.storage_class,
  'role':movie.role,
  'service_account1':movie.service_account1,
  'access_control':movie.access_control,
  'approver':movie.approver } for movie in movies]
  with open('GCS bucket.json', 'w') as json_file:
       json.dump(results, json_file)
  return jsonify({
    'success':True,
    'results':results,
    'count':len(movies)
    
  })
  