package br.ufrj.issuesappthenticator;

import android.animation.Animator;
import android.animation.AnimatorListenerAdapter;
import android.annotation.TargetApi;
import android.app.LoaderManager.LoaderCallbacks;
import android.app.NotificationManager;
import android.content.Context;
import android.content.CursorLoader;
import android.content.Intent;
import android.content.Loader;
import android.content.res.Resources;
import android.database.Cursor;
import android.net.Uri;
import android.os.AsyncTask;
import android.os.Build;
import android.os.Bundle;
import android.provider.ContactsContract;
import android.support.annotation.NonNull;
import android.support.v4.app.NotificationCompat;
import android.support.v7.app.AppCompatActivity;
import android.text.TextUtils;
import android.view.KeyEvent;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.ViewGroup;
import android.view.inputmethod.EditorInfo;
import android.widget.*;
import org.androidannotations.annotations.*;

import java.util.ArrayList;
import java.util.List;

/**
 * A login screen that offers login via email/password.
 */
@EActivity(R.layout.activity_main)
public class MainActivity extends AppCompatActivity {

  // State
  private SavePrefsTask runningSavePrefs = null;

  // Data
  private int humidity = 10;
  private int luminosity = 50;
  private float temperature = 20;

  // UI
  @ViewById
  TextView tempVal;
  @ViewById
  TextView humVal;
  @ViewById
  TextView lightVal;
  @ViewById
  Button tempMinus;
  @ViewById
  Button tempPlus;
  @ViewById
  Button humMinus;
  @ViewById
  Button humPlus;
  @ViewById
  Button lightMinus;
  @ViewById
  Button lightPlus;
  @ViewById
  Button logout;
  @ViewById
  Button save;
  @ViewById
  LinearLayout mainForm;
  @ViewById
  ProgressBar mainProgress;

  @Click({R.id.save})
  void save() {
    if (runningSavePrefs != null) {
      return;
    }

    showProgress(true);
    runningSavePrefs = new SavePrefsTask(humidity, luminosity, temperature);
    runningSavePrefs.execute((Void) null);
  }

  @Click({R.id.logout})
  void logout() {
    Intent gotoPage = new Intent(getBaseContext(), LoginActivity.class);
    startActivity(gotoPage);
  }

  @Click({
      R.id.tempMinus,
      R.id.tempPlus,
      R.id.humMinus,
      R.id.humPlus,
      R.id.lightMinus,
      R.id.lightPlus,
  })
  void changeVal(Button btn) {
    TextView valueView = null;
    ViewGroup row = (ViewGroup) btn.getParent();
    for (int itemPos = 0; itemPos < row.getChildCount(); itemPos++) {
      View view = row.getChildAt(itemPos);
      if (!(view instanceof Button)) {
        valueView = (TextView) view;
        break;
      }
    }

    switch (valueView.getId()){
      case R.id.tempVal:
        if(btn.getText().toString().equals("+")){
          temperature += temperature<50?.5:0;
        }else{
          temperature -= temperature>10?.5:0;
        }
        break;
      case R.id.humVal:
        if(btn.getText().toString().equals("+")){
          humidity += humidity<100?1:0;
        }else{
          humidity -= humidity>0?1:0;
        }
        break;
      case R.id.lightVal:
        if(btn.getText().toString().equals("+")){
          luminosity += luminosity<100?1:0;
        }else{
          luminosity -= luminosity>0?1:0;
        }
    }
    this.setValues();
  }


  @AfterViews
  void setValues() {
    Resources res = getResources();
    tempVal.setText(res.getString(R.string.val_temp, temperature));
    humVal.setText(res.getString(R.string.val_humidity, humidity));
    lightVal.setText(res.getString(R.string.val_light, luminosity));
  }

  //


  @TargetApi(Build.VERSION_CODES.HONEYCOMB_MR2)
  private void showProgress(final boolean show) {
    int shortAnimTime = getResources().getInteger(android.R.integer.config_shortAnimTime);

    mainForm.setVisibility(show ? View.GONE : View.VISIBLE);
    mainForm.animate().setDuration(shortAnimTime).alpha(
        show ? 0 : 1).setListener(new AnimatorListenerAdapter() {
      @Override
      public void onAnimationEnd(Animator animation) {
        mainForm.setVisibility(show ? View.GONE : View.VISIBLE);
      }
    });

    mainProgress.setVisibility(show ? View.VISIBLE : View.GONE);
    mainProgress.animate().setDuration(shortAnimTime).alpha(
        show ? 1 : 0).setListener(new AnimatorListenerAdapter() {
      @Override
      public void onAnimationEnd(Animator animation) {
        mainProgress.setVisibility(show ? View.VISIBLE : View.GONE);
      }
    });
  }

  public class SavePrefsTask extends AsyncTask<Void, Void, Boolean> {

    private final int humidity;
    private final int luminosity;
    private final float temperature;

    SavePrefsTask(int humidity, int luminosity, float temperature) {
      this.humidity = humidity;
      this.luminosity = luminosity;
      this.temperature = temperature;
    }

    @Override
    protected Boolean doInBackground(Void... params) {
      // TODO: attempt authentication against a network service.

      try {
        // Simulate network access.
        // TODO validate password on server
        Thread.sleep(1000);
      } catch (InterruptedException e) {
        return false;
      }

      return true;
    }

    @Override
    protected void onPostExecute(final Boolean success) {
      runningSavePrefs = null;
      showProgress(false);

      Context context = getApplicationContext();

      CharSequence text =
          success?
              "Preferências salvas com sucesso.":
              "Erro salvando preferências, tente novamente.";

      int duration = Toast.LENGTH_LONG;

      Toast toast = Toast.makeText(context, text, duration);
      toast.show();

    }

    @Override
    protected void onCancelled() {
      runningSavePrefs = null;
      showProgress(false);
    }
  }

}
