import {Component, OnInit} from '@angular/core';
import {FormBuilder, Validators} from "@angular/forms";
import {AuthService} from "../auth.service";
import { SHARED_MATERIAL_MODULES } from '../../shared-features/shared-material';
import { StorageService } from '../storage.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [SHARED_MATERIAL_MODULES],
  templateUrl: './register.component.html',
  styleUrl: './register.component.css'
})
export class RegisterComponent implements OnInit {
  registerForm = this.fb.group({
    firstname: ['', Validators.required],
    lastname: ['', Validators.required],
    username: ['', Validators.required],
    email: ['', [Validators.required, Validators.email]],
    password: ['', Validators.required],
    // checkPassword: ['']
  });
  error: string | undefined;

  constructor(
    private fb: FormBuilder,
    private authService: AuthService,
    private storageService: StorageService,
    private router: Router,
  ) {}

  ngOnInit() {}

  onSubmit(): void {
    console.warn(this.registerForm.value);
    this.authService.register(this.registerForm).subscribe({
      next: (data) => {
        console.warn("data ", data)
        this.storageService.saveUser(data);
        this.router.navigate(['/campaign-overview']);
      },
      error: (err) => {
        this.error = 'Login failed';
      }
    });
  }

}
