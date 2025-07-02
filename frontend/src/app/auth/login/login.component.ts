import {Component, OnInit} from '@angular/core';
import {FormBuilder, Validators} from "@angular/forms";
import {AuthService} from "../auth.service";
import {StorageService} from "../storage.service";
import {Router} from "@angular/router";
import { SHARED_MATERIAL_MODULES } from '../../shared-features/shared-material';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [SHARED_MATERIAL_MODULES],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent implements OnInit {
  loginForm = this.fb.group({
    email: ['', [Validators.required, Validators.email]],
    password: ['', Validators.required],
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
    this.authService.login(this.loginForm).subscribe({
      next: (data) => {
        this.storageService.saveUser(data);
        this.router.navigate(['/campaign-overview']);
      },
      error: (err) => {
        this.error = 'Login failed';
      }
    });
  }
}
