package dev.murtaza.firstkotlinapp.api

import dev.murtaza.firstkotlinapp.models.PhotoList
import retrofit2.Call
import retrofit2.http.GET

interface PhotoApi {
    @GET("?key=12661142-9c0a01bede5dc79da56f1dbcf&q=nature&image_type=photo")
    fun getPhoto() : Call<PhotoList>
}