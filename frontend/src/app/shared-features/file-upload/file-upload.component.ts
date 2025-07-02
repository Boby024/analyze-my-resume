import { HttpClient } from '@angular/common/http';
import { Component, Input } from '@angular/core';
import { SHARED_MATERIAL_MODULES } from '../shared-material';

@Component({
  selector: 'app-file-upload',
  standalone: true,
  imports: [SHARED_MATERIAL_MODULES],
  templateUrl: './file-upload.component.html',
  styleUrl: './file-upload.component.css'
})
export class FileUploadComponent {
  fileName = '';

  @Input()
  requiredFileType: string = "text/csv";

  constructor(
    private http: HttpClient
  ) {}

  onFileSelected(event: any) {
    const file:File = event.target.files[0];
    if (file) {
      this.fileName = file.name;
      const formData = new FormData();
      formData.append("file", file);
      console.warn(formData);
      // const upload$ = this.http.post("/api/thumbnail-upload", formData);
      // upload$.subscribe();
    }
  }
}
