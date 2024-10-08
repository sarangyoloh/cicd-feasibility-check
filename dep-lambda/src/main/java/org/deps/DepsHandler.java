package org.deps;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import org.parent.Greet;

public class DepsHandler implements RequestHandler<String, String> {

    @Override
    public String handleRequest(String s, Context context) {
        return new Greet().greet(s);
    }
}
