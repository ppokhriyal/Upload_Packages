from flask import render_template, url_for, flash, redirect, request, abort, session,jsonify
from upload_files import app
from upload_files.forms import BuildIdForm
import os
import os.path
from os import path


@app.route('/')  
def upload():
	form = BuildIdForm()
	return render_template("file_upload_form.html",form=form)



@app.route('/upload_pkg',methods=['GET','POST'])
def upload_pkg():
	form = BuildIdForm()
	if form.validate_on_submit():
		build_id = str(form.firmware_build_id.data)

		#Check build id is valid or not
		if path.isdir('/var/www/html/Firmware-Update-Patch-Records/'+build_id):
			src = '/var/www/html/Firmware-Update-Patch-Records/'+build_id
			dist = '/var/www/html/Upload-Files/pkgs/'+build_id
			os.symlink(src,dist)
			return redirect(url_for('pkg_list',build_id=build_id))
		else:
			flash('Directory Does not Exists','danger')
	return 	render_template("file_upload_form.html",form=form)	


@app.route('/pkgs_list/<int:build_id>',methods=['GET','POST'])
def pkg_list(build_id):

	return render_template("pkg_list.html",build_id=build_id)



@app.route('/boot_upload',methods=['GET','POST'])
def boot_upload():
	if request.method == 'POST':
		f = request.files['file']
		f.save(f.filename)
		flash('File Uploaded Successfully','success')
	return render_template('boot_upload.html')	


@app.route('/success', methods = ['POST'])
def success():

    if request.method == 'POST':
        f = request.files['file']  
        f.save(f.filename)  
        return render_template("success.html", name = f.filename)