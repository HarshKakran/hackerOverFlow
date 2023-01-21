import { Component, OnInit } from '@angular/core';
import {FormGroup, FormBuilder, FormArray, Form} from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';


@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  public experienceNumber: number = 1;
  public projectsNumber: number = 1;
  public skillsNumber: number = 1;
  public achivementsNumber: number = 1
  resumeForm: FormGroup = this.formbuilder.group({
    firstName : [''],
    lastName :[''],
    email: [''],
    linkedin: [''],
    github: [''],
    mobile: [''],
    education : new FormArray([]),
    experience : new FormArray([]),
    project: new FormArray([]),
    skills: new FormArray([]),
    achivements: new FormArray([])
  })
  constructor( private formbuilder : FormBuilder, private http : HttpClient, private router: Router) { }

  ngOnInit(): void {
    this.resumeForm
  }

  get educations(){
    return this.resumeForm.controls["education"] as FormArray
  }
  addEducation() {
    const educationForm = this.formbuilder.group({
      schoolName: [''],
      program:[''],
      startYearEdu:[''],
      endYearEdu:[''],
      cgpa:['']
    });
    this.educations.push(educationForm);
  }
  deleteEducation() {
    this.educations.removeAt(-1);
  }

  get experiences(){
    return this.resumeForm.controls["experience"] as FormArray
  }
  addExperience() {
    // console.log("here")
    const experienceForm = this.formbuilder.group({
      role: [''],
      organisation:[''],
      descriptionExp:[''],
      startYearExp:[''],
      endYearExp:['']
    });
    this.experiences.push(experienceForm);
  }
  deleteExperience() {
    this.experiences.removeAt(-1);
  }

  get projects(){
    return this.resumeForm.controls["projects"] as FormArray
  }
  addProject() {
    const projectForm = this.formbuilder.group({
      name: [''],
      descriptionProj:[''],
      url:[''],
    });
    this.projects.push(projectForm);
  }
  deleteProject() {
    this.projects.removeAt(-1);
  }

  get skills(){
    return this.resumeForm.controls["skills"] as FormArray
  }
  addSkill() {
    const skillForm = this.formbuilder.group({
      skillName: ['']
    });
    this.skills.push(skillForm);
  }
  deleteSkill(){
    this.skills.removeAt(-1)
  }

  get achivements(){
    return this.resumeForm.controls["achivements"] as FormArray
  }
  addAchivements() {
    const achivementForm = this.formbuilder.group({
      achivementName: ['']
    });
    this.skills.push(achivementForm);
  }
  deleteAchivement(){
    this.achivements.removeAt(-1)
  }
  saveResume(){
    console.log(this.resumeForm.controls)
    // console.log(this..controls)
    console.log("save")
    // this.router.navigate(['dashboard'])
  }
  changeEductionNumber( val: boolean ): void {
    // console.log("here")
    // if (val == true) {this. += 1}
    // else {if (this.educationNumber>1) this.educationNumber -=1}
  }
  changeExperienceNumber( val: boolean ): void {
    // console.log("here")
    if (val == true) {this.experienceNumber += 1}
    else {if (this.experienceNumber>1) this.experienceNumber -=1}
  }
  changeProjectsNumber( val: boolean ): void {
    // console.log("here")
    if (val == true) {this.projectsNumber += 1}
    else {if (this.projectsNumber>1) this.projectsNumber -=1}
  }
  changeSkillsNumber(val:boolean ): void {
    // console.log("here")
    if (val == true) {this.skillsNumber += 1}
    else {if (this.skillsNumber>1) this.skillsNumber -=1}
  }
  changeAchivementsNumber(val:boolean ): void {
    // console.log("here")
    if (val == true) {this.achivementsNumber += 1}
    else {if (this.achivementsNumber>1) this.achivementsNumber -=1}
  }

}
