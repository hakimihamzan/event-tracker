package com.k31.testingallofapp;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.Manifest;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

import com.budiyev.android.codescanner.CodeScanner;
import com.budiyev.android.codescanner.CodeScannerView;
import com.budiyev.android.codescanner.DecodeCallback;
import com.google.zxing.Result;
import com.karumi.dexter.Dexter;
import com.karumi.dexter.PermissionToken;
import com.karumi.dexter.listener.PermissionDeniedResponse;
import com.karumi.dexter.listener.PermissionGrantedResponse;
import com.karumi.dexter.listener.PermissionRequest;
import com.karumi.dexter.listener.single.PermissionListener;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class ScanActivity extends AppCompatActivity {
    CodeScannerView codeScannerView;
    CodeScanner mCodeScanner;
    TextView resultTextView;
    String otp = "";
    EvenTrackersApi evenTrackersApi;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_scan);
        codeScannerView = (CodeScannerView) findViewById(R.id.scannerView);
        resultTextView = findViewById(R.id.resultTextView);

        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("https://eventrackers.pythonanywhere.com")
                .addConverterFactory(GsonConverterFactory.create())
                .build();

        evenTrackersApi = retrofit.create(EvenTrackersApi.class);

        mCodeScanner = new CodeScanner(this, codeScannerView);

        mCodeScanner.setDecodeCallback(new DecodeCallback() {
            @Override
            public void onDecoded(@NonNull Result result) {
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        String temp = result.getText();
                        String[] split = temp.split("TP : ");
                        otp = split[1];
                        System.out.println("---------------"+otp);
                        createPost();
                        finish();
                    }
                });
            }
        });

        codeScannerView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                mCodeScanner.startPreview();
            }
        });


    }

    @Override
    protected void onResume() {
        super.onResume();
        requestCameraPermission();
    }

    private void requestCameraPermission() {
        Dexter.withContext(this).withPermission(Manifest.permission.CAMERA).withListener(new PermissionListener() {
            @Override
            public void onPermissionGranted(PermissionGrantedResponse permissionGrantedResponse) {
                mCodeScanner.startPreview();
            }

            @Override
            public void onPermissionDenied(PermissionDeniedResponse permissionDeniedResponse) {
                Toast.makeText(ScanActivity.this, "You need camera to scan qr code", Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onPermissionRationaleShouldBeShown(PermissionRequest permissionRequest, PermissionToken permissionToken) {

                permissionToken.continuePermissionRequest();
            }
        }).check();
    }

    private void createPost() {
        Post post = new Post("Kimi from android but with qr", 2017267524, "BM246","Accountancy", "Kb", "Also Kb","05.34", "MGT531", "SYamim", otp);

        Call<Post> call = evenTrackersApi.createPost(post);
//        Call<Post> call = evenTrackerApi.createPost("Kimi from android but from urlencoded", 2017267524, "BM246","Accountancy", "Kb", "Also Kb","05.34", "MGT531", "SYamim", "CiEggrGin4428856");
        call.enqueue(new Callback<Post>() {
            @Override
            public void onResponse(Call<Post> call, Response<Post> response) {
                if (!response.isSuccessful()) {
                    resultTextView.setText("Code: " + response.code());
                    Toast.makeText(ScanActivity.this, "Error loggin in, Code: "+response.code(), Toast.LENGTH_SHORT).show();
                    return;
                }

                Toast.makeText(ScanActivity.this, "Checking in succeed!", Toast.LENGTH_SHORT).show();


//
//                Post postResponse = response.body();
//
//                String content = "";
//                content += "Code: " + response.code() + "\n";
//                content += "ID: " + postResponse.getId() + "\n";
//                content += "Name: " + postResponse.getName() + "\n";
//                content += "Student ID: " + postResponse.getStudentId() + "\n";
//                content += "Programme Code: " + postResponse.getProgrammeCode() + "\n";
//                content += "Faculty: " + postResponse.getFaculty() + "\n";
//                content += "Campus: " + postResponse.getCampus() + "\n";
//                content += "Location: " + postResponse.getLocation() + "\n";
//                content += "Time: " + postResponse.getTime() + "\n";
//                content += "Class Attended: " + postResponse.getClassAttended() + "\n";
//                content += "Lecturer: " + postResponse.getLecturer() + "\n";
//                content += "Unique Number: " + postResponse.getUnique() + "\n\n";
//
//                resultTextView.setText(content);

            }

            @Override
            public void onFailure(Call<Post> call, Throwable t) {
//                resultTextView.setText(t.getMessage());
                Toast.makeText(ScanActivity.this, "Error loggin in"+t.getMessage(), Toast.LENGTH_SHORT).show();
                System.out.println("-----------" + t.getCause());
            }
        });

    }


}