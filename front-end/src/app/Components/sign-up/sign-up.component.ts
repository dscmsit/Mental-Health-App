import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.css'],
})
export class SignUpComponent{
  // constructor(private http:HttpClient){}
  // ngOnInit(): void {
  //   throw new Error('Method not implemented.');
  // }
  // changeGender(e:any){
  //   this.gender
  // }
  // onSubmit(){
  //   const reg={
  //     first_name:this.first_name,
  //     last_name:this.last_name,
  //     email:this.email,
  //     password:this.password,
  //     confirm_pass:this.confirm_pass,
  //     dob:this.dob,
  //     gender:this.gender
  //   }
  //   console.warn(reg)
  //   if(reg.first_name==""){
  //     console.log("field cannot be empty")
  //   }

  // }

  Gender: any = ['Male', 'Female', 'Others'];

  constructor(public fb: FormBuilder, private http: HttpClient,  private router:Router) {}
  registrationForm = this.fb.group({
    stateName: ['', [Validators.required]],
    genderName: ['', [Validators.required]],
    first_name: ['', [Validators.required]],
    last_name: ['', [Validators.required]],
    email: ['', [Validators.required]],
    password: ['', [Validators.required]],
    confirm_pass: ['', [Validators.required]],
    dob: ['', [Validators.required]],
    
  });


  changeGender(e: any) {
    this.genderName?.setValue(e.target.value, {
      onlySelf: true,
    });
  }
  changeState(e: any){
    this.stateName?.setValue(e.target.value,{
      onlySelf: true,
    });
  }
  // Access formcontrols getter
  get genderName() {
    return this.registrationForm.get('genderName');
  }
  get first_name() {
    return this.registrationForm.get('first_name');
  }
  get last_name() {
    return this.registrationForm.get('last_name');
  }
  get email() {
    return this.registrationForm.get('email');
  }
  get password() {
    return this.registrationForm.get('password');
  }
  get confirm_pass() {
    return this.registrationForm.get('confirm_pass');
  }
  get dob() {
    return this.registrationForm.get('dob');
  }
  get stateName(){
    return this.registrationForm.get('stateName')
  }
  res:any;
  onSubmit() {
    // console.warn(this.registrationForm.);
    if (
      this.registrationForm.value.confirm_pass !==
      this.registrationForm.value.password
    ) {
      // continue
      alert('passwords do not match');
    }
    const stringData = JSON.stringify(this.registrationForm.value); // data is a string you have to convert to json object
    const data = JSON.parse(stringData); // data is now a JS object

    const userData = {
      header: 'register',
      data: data,
    };

    this.http
      .post('https://mentalhealthbackend.onrender.com/register', userData, {
        headers: {
          'Content-Type': 'application/json',
        },
      })
      .subscribe((result) => {
        this.res = result;
        if(this.res.status == "true"){
          localStorage.setItem('login_status','true');
          localStorage.setItem('user_id',this.res.id);
          this.router.navigate(['/']); 
          setTimeout(()=>{
            window.location.reload();
       
           },1000)
        }
        console.log(localStorage.getItem('login_status'));
        console.log(localStorage.getItem('user_id'));
        
      });
    // window.location.reload();

  }
}
