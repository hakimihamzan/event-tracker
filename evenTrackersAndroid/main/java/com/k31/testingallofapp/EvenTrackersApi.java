package com.k31.testingallofapp;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.Field;
import retrofit2.http.FormUrlEncoded;
import retrofit2.http.GET;
import retrofit2.http.POST;

public interface EvenTrackersApi {
    @GET("/--api/participants/")
    Call<List<Post>> getPosts();

    @POST("/--api/participants/")
    Call<Post> createPost(@Body Post post);

    @FormUrlEncoded
    @POST("/--api/participants/")
    Call<Post> createPost(
            @Field("name") String name,
            @Field("student_id") int student_id,
            @Field("programme_code") String programme_code,
            @Field("faculty") String faculty,
            @Field("campus") String campus,
            @Field("location") String location,
            @Field("time") String time,
            @Field("class_attended") String class_attended,
            @Field("lecturer") String lecturer,
            @Field("unique") String unique
    );

}
